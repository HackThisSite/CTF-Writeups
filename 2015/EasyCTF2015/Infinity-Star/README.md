Description:
Solved by 99 teams.

Infinity Star Bank's new website is up! In honor of their opening, they are offering a premium service that allows you to view flags.
Important note: the account michael is an admin account.

So, upon going to the website (with the account name blah), there isn't much we can do without first registering an account and logging in. So, registering was done after a few simple SQLi attempts just to see.
Upon logging in, the greeting screen displays the following important pieces of text:
Welcome, blah.
Head over to the Account page to make transfers.
For just $99.99 ($0.01 tax), you can get our Premium Infinity service, allowing you to view the flag.
I headed over to the Account page and I seen the form request to transfer money to other accounts. I cracked open the source code, and noticed the form being sent via GET XML HTTP Requests via what appears to be jQuery.
Transfer Source Code:

```
var transfer_funds = function() {
	var disable = "input";
	$(disable).attr("disabled", "disabled");
	$.getJSON("/api/bank/transfer", {
		amount: $("#amount").val(),
		recipient: $("#recipient").val()
	}, function(result) {
		display_message("#transfer_msg", (result.success == 1 ? "success" : "danger"), result.message, function() {
		if (result.success == 1) { location.reload(true); }
			else { $(disable).removeAttr("disabled"); }
		});
	});
};
```

The one note to take from this script is that there isn't any type of unique strings being passed with the request, which would make it something similar to the following in the URL:
`/api/bank/transfer?amount=<Money Total To Transfer Here>&recipient=<User Account Name Here>`
I started over-thinking the challenge completely and immediately changed the API to point towards my public server to a URL like `/index.php?blargity=blarg?`
I tailed my server logs and seen that the request was coming through, so that's a good sign. I then noticed a report page feature at the bottom of the website, which states that the reporting page would be reviewed by an admin. This bit of information made it blantly obvious to me that this was a XSRF challenge, and our entry point of attack was there. The code for the report page is as follows:
Report Problem page Code:

```
var report_problem = function() {
	var el = document.createElement("a");
	el.href = $("#page").val(); // to get full path
	$.post("/api/report", { page: el.href }, function(result) {
		$("#myModal").modal("hide");
	});
}
```

Where our HTML code for the page list is in the following format:
```
<option selected="" value="/index">Home</option>
```
The obvious thing to do at this point was to replace the value with that of the following URL:
`/api/bank/transfer?amount=1000&recipient=blah`
After this is reported, the admin views the page, which then performs the bank transfer script and hapilly transfers $1000 into the account belonging to blah, which is our account in this scenario. After this was completed, I was able to purchase what was necessary to view the flag.
The flag is: `easyctf{csrf_protection_would_probably_have_been_a_good_idea_:/}`
