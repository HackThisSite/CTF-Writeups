## Postman
* Web Exploitation
* Kyle made an super secure website only accesible by the Google Ultron browser. Figure out how to login to <link>
* 50 points


This was a pretty cool problem!

So when you go to the website you get:
>Error: Unauthorized browser <Your browser's user agent> detected. Only users of "Google Ultron" may access this page."

To remedy this, you had to edit your "user-agent" HTTP-header. The user-agent header tells the website which browser you are using. Headers essentially tell a website about your browsing session, and are included every time you visit a website. 
For more info about headers read the Wikipedia page: <https://en.wikipedia.org/wiki/List_of_HTTP_header_fields>

Once you change your user-agent string to Google Ultron, and revisit the website, the website returns
>Error: "SpecialAuth" header not set to my name

SpecialAuth is not a standard HTTP-Header, so you must add it as a request property when you visit the website, and set its value to Kyle.
You know it is Kyle from the problem statement.
So once the "SpecialAuth" header is set to Kyle, the website returns:

>Error: This site must be accessed from "kyleisacoolguy.org"

The HTTP-Header that tells the server your last website is known as the "referer" so you must set the referer header to that website.
Once all that is done, you get the answer:

    Successfully Authenticated! Your flag is:lasactf{h3aders_ar3_c00l}

Attached as a separate file is my java code to complete this challenge. 
