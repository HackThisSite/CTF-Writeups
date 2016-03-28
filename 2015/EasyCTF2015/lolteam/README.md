Description: Solved by 753 teams.
There's a suspicious team out there called lolteam, I got my eyes on them for a while and I managed to [wiretap](https://www.easyctf.com/static/problems/lolteam/lolteam.pcapng) their browser as they were changing their password. What did they change their password to?

Upon following the link, we get a file called `lolteam.pcapng` which is a packet capture file. To open it, we needed a packet analyzer. We used [Wireshark](https://www.wireshark.org) for that purpose.
Once the file was loaded into Wireshark, we began analyzing.
Since the description mentioned of changing password and knowing that most of the forms use `POST` request for such actions, we began looking for such requests. We found a row which was interesing on the "Packet List" pane of Wireshark:

``` 4	0.009564000	2601:248:2:7b20:8544:d211:3048:e8c2	2400:cb00:2048:1::681c:84e	HTTP	864	POST /api/account/update HTTP/1.1  (application/x-www-form-urlencoded)```

Upon selecting the row and viewing the packet details on "Packet Details" pane, we saw a field titled `HTML Form URL Encoded: application/x-www-form-urlencoded`. Expanding the field, we saw a field which had following text:

``` Form item: "password" = "flag{no,_lolteam_is_not_an_admin_account}" ``` 

After making slight changes, we found the flag to be `easyctf{no,_lolteam_is_not_an_admin_account}`
