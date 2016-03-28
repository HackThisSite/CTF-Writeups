require 'chunky_png'
coords = Array.new
string = gets
reg = /\((\d+), (\d+)\)/
coords = string.scan(reg)
n = 0;
coords.each do |x|
    x.each do |y|
        n = y.to_i if y.to_i > n
    end
end
image = ChunkyPNG::Image.new(n+1,n+1,ChunkyPNG::Color::BLACK)
coords.each do |x|
    image[x[0].to_i,x[1].to_i] = ChunkyPNG::Color::WHITE
end
image.save("qr.png") 
