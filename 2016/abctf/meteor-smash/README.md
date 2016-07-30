# Metor Smash
> Dig around in this [blog](http://107.170.122.6:8082/ "blog") and I'm sure you can find a flag.

This challenge is a simple blog site created using Meteor. Meteor ships out by default with a package called `insecure`
which allows a lot of vulnerabilites. However, after doing some tests, I concluded that the package was in fact disabled.
Popping open the source code for the `app.js` file revealed an interesting piece of commented out logic:
`if(user.profile && user.profile.admin)`

Now we know what our goal is. We need to set these values to true in our account, or try something else to get this logic to evaluate and spit out our flag.
The following does exactly that for us:

`Meteor.users.update(Meteor.userId(), {$set: {"profile.admin": true}});`

After executing, the view of the blog will modify and the flag portion will be revealed at refresh:

`ABCTF{r3lly_s3cure_Auth0riz4t1on}`
