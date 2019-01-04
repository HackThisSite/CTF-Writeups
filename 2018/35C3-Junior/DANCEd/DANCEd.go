package main

import (
	"fmt"
	"net"
	"os"
	"crypto/rand"
	"time"
	"bufio"
	"io/ioutil"
	"strconv"
	"math/bits"
	"encoding/binary"
	"encoding/hex"
	"bytes"
	"strings"
	"sync"
)

const (
	HOST = "localhost"
	PORT = "11520"
)

var nonce [2]uint32
var mutex = &sync.Mutex{}


func check(e error){
	if e != nil {
        panic(e)
    }
}


func showWelcomeMSG(c net.Conn) {
	header := []byte(`
	 _______    ______   __    __   ______   ________       __ 
	|       \  /      \ |  \  |  \ /      \ |        \     |  \
	| $$$$$$$\|  $$$$$$\| $$\ | $$|  $$$$$$\| $$$$$$$$ ____| $$
	| $$  | $$| $$__| $$| $$$\| $$| $$   \$$| $$__    /      $$
	| $$  | $$| $$    $$| $$$$\ $$| $$      | $$  \  |  $$$$$$$
	| $$  | $$| $$$$$$$$| $$\$$ $$| $$   __ | $$$$$  | $$  | $$
	| $$__/ $$| $$  | $$| $$ \$$$$| $$__/  \| $$_____| $$__| $$
	| $$    $$| $$  | $$| $$  \$$$ \$$    $$| $$     \\$$    $$
	 \$$$$$$$  \$$   \$$ \$$   \$$  \$$$$$$  \$$$$$$$$ \$$$$$$$`  + "\n\n")
	welcome_msg := []byte("           Welcome to the world's first cryptographically secure\n            sign-up platform for the dance class of your dream!\n")
	line := []byte("\n\n############################################################################\n\n")
	c.Write(line)
	c.Write(header)
	c.Write(welcome_msg)
	c.Write(line)
}


func doubleRound(block *[4][4]uint32){
	for i := 0; i < 4; i++ {
        block[(1 + i) % 4][i] = block[(1 + i) % 4][i] ^ bits.RotateLeft32(block[(0 + i) % 4][i] + block[(3 + i) % 4][i], 7)
        block[(2 + i) % 4][i] = block[(2 + i) % 4][i] ^ bits.RotateLeft32(block[(1 + i) % 4][i] + block[(0 + i) % 4][i], 9)
        block[(3 + i) % 4][i] = block[(3 + i) % 4][i] ^ bits.RotateLeft32(block[(2 + i) % 4][i] + block[(1 + i) % 4][i], 13)
        block[(0 + i) % 4][i] = block[(0 + i) % 4][i] ^ bits.RotateLeft32(block[(3 + i) % 4][i] + block[(2 + i) % 4][i], 18)
    }
    for i := 0; i < 4; i++ {
        block[i][(1 + i) % 4] = block[i][(1 + i) % 4] ^ bits.RotateLeft32(block[i][(0 + i) % 4] + block[i][(3 + i) % 4], 7)
        block[i][(2 + i) % 4] = block[i][(2 + i) % 4] ^ bits.RotateLeft32(block[i][(1 + i) % 4] + block[i][(0 + i) % 4], 9)
        block[i][(3 + i) % 4] = block[i][(3 + i) % 4] ^ bits.RotateLeft32(block[i][(2 + i) % 4] + block[i][(1 + i) % 4], 13)
        block[i][(0 + i) % 4] = block[i][(0 + i) % 4] ^ bits.RotateLeft32(block[i][(3 + i) % 4] + block[i][(2 + i) % 4], 18)
    }
}

func doubleunRound(block *[4][4]uint32){

    for i := 3; i >= 0; i-- {

        block[i][(0 + i) % 4] = block[i][(0 + i) % 4] ^ bits.RotateLeft32(block[i][(3 + i) % 4] + block[i][(2 + i) % 4], 18)

        block[i][(3 + i) % 4] = block[i][(3 + i) % 4] ^ bits.RotateLeft32(block[i][(2 + i) % 4] + block[i][(1 + i) % 4], 13)


        block[i][(2 + i) % 4] = block[i][(2 + i) % 4] ^ bits.RotateLeft32(block[i][(1 + i) % 4] + block[i][(0 + i) % 4], 9)

        block[i][(1 + i) % 4] = block[i][(1 + i) % 4] ^ bits.RotateLeft32(block[i][(0 + i) % 4] + block[i][(3 + i) % 4], 7)
    }

	for i := 3; i >= 0; i-- {

        block[(0 + i) % 4][i] = block[(0 + i) % 4][i] ^ bits.RotateLeft32(block[(3 + i) % 4][i] + block[(2 + i) % 4][i], 18)

        block[(3 + i) % 4][i] = block[(3 + i) % 4][i] ^ bits.RotateLeft32(block[(2 + i) % 4][i] + block[(1 + i) % 4][i], 13)

        block[(2 + i) % 4][i] = block[(2 + i) % 4][i] ^ bits.RotateLeft32(block[(1 + i) % 4][i] + block[(0 + i) % 4][i], 9)

        block[(1 + i) % 4][i] = block[(1 + i) % 4][i] ^ bits.RotateLeft32(block[(0 + i) % 4][i] + block[(3 + i) % 4][i], 7)
    }
}

func generateKeyStream(count uint32) []byte {
	key := [8]uint32{0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff}
	block := [4][4]uint32{
        {0x61707865, key[0], key[1], key[2]},
        {key[3], 0x3320646e, nonce[0], nonce[1]},
        {count, 0x00000000, 0x79622d32, key[4]},
		{key[5], key[6], key[7], 0x6b206574}}

  /*
  fmt.Printf("Original:\n");
  for c := 0; c < 4; c++ {
		for r := 0; r < 4; r++ {
			fmt.Printf("%08x ", block[c][r]);
		}
		fmt.Printf("\n");             
	}
*/  
  //fmt.Printf("After round:\n");
	for i := 0; i < 10; i++ {
		doubleRound(&block)
	}/*
	for c := 0; c < 4; c++ {
		for r := 0; r < 4; r++ {
			fmt.Printf("%08x ", block[c][r]);
		}
		fmt.Printf("\n");             
	}*/
	
	var stream []byte
	current := make([]byte, 4)
	for c := 0; c < 4; c++ {
		for r := 0; r < 4; r++ {
			binary.LittleEndian.PutUint32(current, block[c][r])
			stream = append(stream, current...)
        }
	}
	return stream
}


func encrypt(msg string, count uint32) []byte {
	stream := generateKeyStream(count)
	cipher := make([]byte, len(msg))
	for i := 0; i < len(msg) && i < 64; i++ {
		cipher[i] = byte(msg[i]) ^ stream[i]
	}
	return cipher
}

func decrypt(msg string, count uint32) []byte {
	stream := generateKeyStream(count)
	cipher := make([]byte, len(msg))
  tmp := make([]byte, len(msg)/2)
  l, _ := hex.Decode(tmp, []byte(msg))
	for i := 0; i < l && i < 64; i++ {
		cipher[i] = tmp[i] ^ stream[i]
	}
	return cipher
}

func optTest(c net.Conn) {
	c.Write([]byte("\n"))
  c.Write([]byte("testing\n"))

	bufMSG := make([]byte, 65)
	c.Write([]byte("\n           Enter the plain message: "))
  bufReader := bufio.NewReader(c)
	n, _ := bufReader.Read(bufMSG)
	if n < 2 || n > 65 {
		c.Write([]byte("\n           Abort.\n"))
		return
	}
  bufReader.Reset(c)
  bufTOKEN := make([]byte, 65*2)
	c.Write([]byte("\n           Enter the token: "))
	i, _ := bufReader.Read(bufTOKEN)
  //token is twice as long since its a hex representation
	if i < 2 || i > 129 {
		c.Write([]byte("\n           Abort.\n"))
		return
	}
  bufRAW := make([]byte, 65)
  j, _ := hex.Decode(bufRAW, bufTOKEN)
  if j < 2 || j > 65 {
		c.Write([]byte("\n           Abort.\n"))
		return
	}
  c.Write([]byte("converting back to bytes..\n"));
  
  //extracting stream
  strm := make([]byte, len(bufMSG))
  for i := 0; i < len(bufMSG) && i < 64; i++ {
		strm[i] = byte(bufMSG[i]) ^ bufRAW[i]
	}

block := [4][4]uint32{
        {0x61707865, 0xFF, 0xFF, 0xFF},
        {0xFF, 0x3320646e, 0xFF, 0xFF},
        {0xFF, 0x00000000, 0x79622d32, 0xFF},
		{0xFF, 0xFF, 0xFF, 0x6b206574}}
  //block := make([][]uint32, 4)
  //for i := 0; i < 4; i++ {
  //  block[i] = make([]uint32, 4)
  //}
  tmp := make([]byte, 4)
  i = 0
  for c := 0; c < 4; c++ {
 		for r := 0; r < 4; r++ {
		  for h := 0; h < 4; h++ {
        tmp[h] = strm[i]
        i++
      }
      block[c][r] = binary.LittleEndian.Uint32(tmp)
		}          
	}
  
  fmt.Printf("Retrieved: \n");
  for c := 0; c < 4; c++ {
		for r := 0; r < 4; r++ {
			fmt.Printf("%08x ", block[c][r]);
		}
		fmt.Printf("\n");             
	}

  
  for i := 0; i < 10; i++ {
		doubleunRound(&block)
	}

  
  fmt.Printf("Unrounded\n");
  for c := 0; c < 4; c++ {
		for r := 0; r < 4; r++ {
			fmt.Printf("%08x ", block[c][r]);
		}
		fmt.Printf("\n");             
	}
}

func optBook(c net.Conn) {
	c.Write([]byte("\n"))
	c.Write([]byte("            #   |   Dance   |  slots\n"))
	c.Write([]byte("           --------------------------\n"))
	c.Write([]byte("           (1)  |   Tango   |    8\n"))
	c.Write([]byte("           (2)  |   Salsa   |    8\n"))
	c.Write([]byte("           (3)  |  Cha-Cha  |    8\n\n"))
	c.Write([]byte("           >> "))
	bufCMD := make([]byte, 2)
	bufReader := bufio.NewReader(c)
	bufReader.Read(bufCMD)
	bufReader.Reset(c)

	var pre string
	switch string(bufCMD[0]) {
	case "1":
		pre = "tango "
	case "2":
		pre = "salsa "
	case "3":
		pre = "chacha "
	default:
		return
	}

	bufNAME := make([]byte, 65)
	c.Write([]byte("\n           Enter your full name: "))
	n, _ := bufReader.Read(bufNAME)
	if n < 2 || n > 65 - len(pre) {
		c.Write([]byte("\n           Abort.\n"))
		return
	}

	msg := pre + string(bufNAME[:n-1])
	fmt.Println("\"" + msg + "\"")
	
	mutex.Lock()
	var count uint32
	f, e := os.OpenFile("reservations.txt", os.O_CREATE|os.O_APPEND|os.O_RDWR, 0644)
	check(e)
	scanner := bufio.NewScanner(f)
	count = 0
	for scanner.Scan() {
    	count++
	}
	fmt.Printf("%08x\n", count)
	token := encrypt(msg, count)
	reservationMessage := fmt.Sprintf("%x\n", token)
	_, e = f.Write([]byte(reservationMessage))
	check(e)
	f.Close()
	mutex.Unlock()
	
	fmt.Printf(reservationMessage)
	tokenPreparedMessage := fmt.Sprintf("\n           Your token: %x\n", token)
	c.Write([]byte(tokenPreparedMessage))
	c.Write([]byte("           If you lose your token, you will not be eligible to participate.\n\n"))
}



func optHax(c net.Conn){
  var count uint32
	f, e := os.OpenFile("dump.txt", os.O_CREATE|os.O_APPEND|os.O_RDWR, 0644)
	check(e)
	scanner := bufio.NewScanner(f)
	count = 0
  tmp := make([]byte, 56*3)
  c.Write([]byte("dumping"))
	for scanner.Scan() {
      c.Write([]byte("\nencrypted: "))
      c.Write([]byte(scanner.Text()))
      tmp = decrypt(scanner.Text(), count)
      c.Write([]byte("\ndecrypted: "))
      c.Write(tmp)
    	count++
	}

}

func optShow(c net.Conn){
	content, e := ioutil.ReadFile("reservations.txt")
	if e != nil {
		c.Write([]byte("\n"))

	} else {
		c.Write([]byte("\nReservations:\n"))
		c.Write(content)
		c.Write([]byte("\n"))
	}
}


func optInfo(c net.Conn) {
	c.Write([]byte("\n           "))
	c.Write([]byte("DANCE LIKE NOBODY IS WATCHING!\n"))
	c.Write([]byte("           "))
	c.Write([]byte("ENCRYPT LIKE EVERYBODY IS!\n\n"))
	c.Write([]byte("           "))
	c.Write([]byte("Blockchain secured payments coming soon!\n\n"))
}


func optDBG(c net.Conn) {
	timeout := 1200 * time.Millisecond
	bufReader := bufio.NewReader(c)
	c.SetReadDeadline(time.Now().Add(timeout))
	_, e := bufReader.ReadBytes('\n')
	if e == nil {
		b, e := ioutil.ReadFile("DANCEd.go")
		check(e)
		c.Write([]byte(strconv.Itoa(len(b)) + "\n"))
		c.Write(b)
	} else {
		c.Write([]byte("\n           Goodbye!\n\n"))
	}
	c.Close()
}


func showHelp(c net.Conn) {
	c.Write([]byte("           (1) Book a Class\n           (2) Show Bookings\n           (3) More Information\n\n"))
}


func handleConnection(c net.Conn) {
	showWelcomeMSG(c)
	showHelp(c)
	bufReader := bufio.NewReader(c)
	inputLoop: for {
		bufReader.Reset(c)
		c.Write([]byte("           > "))
		buf := make([]byte, 2)
		bufReader.Read(buf)
		
		switch string(buf[0]) {
		case "1":
			optBook(c)
		case "2":
			optShow(c)
		case "3":
			optInfo(c)
		case "0":
			optDBG(c)
    case "t":
      optTest(c)
    case "d":
      optHax(c)
		case "h":
			c.Write([]byte("\n"))
			showHelp(c)
		default:
			break inputLoop
		}
	}
	c.Write([]byte("\n           Goodbye!\n\n"))
	c.Close()
}


func setNonce() {
	nonceFileCont, e := ioutil.ReadFile("nonce.txt")
	n0 := make([]byte, 4)
	n1 := make([]byte, 4)
	if e != nil {
		_, e := rand.Read(n0)
		check(e)
		_, e = rand.Read(n1)
		check(e)
		nonceString := fmt.Sprintf("%08x %08x", n0, n1)
		ioutil.WriteFile("nonce.txt", []byte(nonceString), 0644)
		check(e)
	} else {
		nonceSplit := strings.Split(string(nonceFileCont), " ")
		n0, e = hex.DecodeString(nonceSplit[0])
		n1, e = hex.DecodeString(nonceSplit[1])
	
	}
	_ = binary.Read(bytes.NewReader(n0), binary.BigEndian, &nonce[0])
	_ = binary.Read(bytes.NewReader(n1), binary.BigEndian, &nonce[1])
	fmt.Printf("nonce: 0x%08x 0x%08x\n", nonce[0], nonce[1])
}


func main() {
	l, e := net.Listen("tcp", HOST+":"+PORT)
	check(e)
	defer l.Close()
	
	setNonce()
	
	for {
		conn, e := l.Accept()
		check(e)
		go handleConnection(conn) 
	}
}
