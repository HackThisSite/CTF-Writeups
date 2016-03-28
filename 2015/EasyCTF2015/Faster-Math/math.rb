#!/usr/bin/ruby
require 'socket'

HOST      = 'programming.easyctf.com'
PORT      = 10300
LOG_FILE  = 'server-log.txt'
FILE      = open(LOG_FILE, 'w')

@sock = TCPSocket.new(HOST, PORT)

def send_data(data)
  @sock.write("#{data.to_s}\n")
  puts "Sent Solution: #{data}"
  FILE.write("WE SENT: #{data.to_s}\n")
end

def operations(data)
  xplode = data.split(':')[1].split('=')
  math, answer = xplode[0].strip, xplode[1].strip
  locs, stop = [], false
  (0..2).map { |i| locs.push(math.index('_')); math[locs[i]] = '~' }

  ops = '+++++-++*+-++--+-*+*++*-+**-++-+--+*--+-----*-*+-*--***++*+-*+**-+*--*-***+**-***'

  until stop == true
    cur_ops = ops[0..2]
    ops.slice!(0..2)
    (0..2).map { |x| math[locs[x]] = cur_ops[x] }
    if eval(math) == answer.to_i
      stop = true
    end
  end
  send_data(cur_ops.gsub('*', 'x'))
end

def finding_root(data, eq)
  n = data.split('x')
  a = n[0].delete(' ')
  b = n[1].split('^2 ')[1].delete(' ')
  c = n[2].delete(' ')
  solution = %x(python root.py -#{eq} #{a} #{b} #{c})
  send_data(solution)
end

def projected(data)
  measurements = data.scan(/ (\d+) /).join(' ').split(' ').map(&:to_i)
  velocity    = measurements[0]
  height      = measurements[1]
  grav_const  = measurements[3]
  time = Math.sqrt(height * 2 / grav_const)
  disp = velocity * time
  send_data(disp.to_i.to_s)
end

def coins(data)
  coins = {
    "ten-dollar"    => 1000,
    "five-dollar"   => 500,
    " dollar "      => 100,
    "half-dollar"   => 50,
    "quarters"      => 25,
    "dimes"         => 10,
    "nickels"       => 5,
    "pennies"       => 1,
  }
  hits = []
  total = data.split('for my')[1].split('purchase')[0].delete(' ').gsub('$','')

  coins.map { |name, val| hits.push(val) if data.include?(name) }

  call = "python coins.py #{total} #{hits.join(' ')}"
  solution = %x( #{call} )
  send_data(solution)
end

loop do
  data = @sock.recv(1024)
  puts data unless data.nil?
  FILE.write(data) unless data.nil?

  if data.to_s.include?('operations')
    operations(data.to_s)
  elsif data.to_s.include?('projected')
    projected(data.to_s)
  elsif data.to_s.include?('root:')
      if data.include?('lesser')
        finding_root(data.to_s.split(': ')[1], 'l')
      else
        finding_root(data.to_s.split(': ')[1], 'g')
      end
  elsif data.to_s.include?('purchase')
    coins(data.to_s)
  end
end
