#Elemental
> Just put in the password for the flag! [Link](http://yrmyzscnvh.abctf.xyz/web1/ "link")

This challenge was so easy it's almost too boring to do a writeup for. Anyway...

The site has a password input box, and the goal is to find the password. Upon viewing the page source, we notice a small html comment:

`<!-- 7xfsnj65gsklsjsdkj -->`

After attempting to use `7xfsnj65gsklsjsdkj` in the password field, we get a quick popup that lasts roughly 2-3 seconds with the flag in it:

`ABCTF{insp3ct3d_dat_3l3m3nt}`
