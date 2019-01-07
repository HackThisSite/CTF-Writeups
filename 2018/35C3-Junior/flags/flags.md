# Flags

>Solves: 411

>Fun with flags: http://35.207.132.47:84

>Flag is at /flag

>Difficulty estimate: Easy

## Analysis

Site displays it's own PHP source code

```php
<?php
  highlight_file(__FILE__);
  $lang = $_SERVER['HTTP_ACCEPT_LANGUAGE'] ?? 'ot';
  $lang = explode(',', $lang)[0];
  $lang = str_replace('../', '', $lang);
  $c = file_get_contents("flags/$lang");
  if (!$c) $c = file_get_contents("flags/ot");
  echo '<img src="data:image/jpeg;base64,' . base64_encode($c) . '">';
```
Server takes Accept-Laguage header , uses str_replace to remove "../" from it (attempt to defend against directory traversal)
then uses file_get contents to grab file from flags directory whose filename corresponds to Accept-Language header.

Finally it includes file in page as image, base64 encoded.

## Solution

This is pretty classic filter bypass directory traversal challenge. Problem with using str_replace for filtering is that it only does one pass over the string.
If Accept-Language header is set to "../../../../../flag" all "../" would be removed leaving us with only "flag".
However if we set it to "....//....//....//....//....//flag" it will become "../../../../../flag"!

We don't have flag just yet, we need to download "image" we got and base64 decode it.

```bash
$ base64 -d flag
35c3_this_flag_is_the_be5t_fl4g
```

For more info on directory traversal see this [wikipedia article](https://en.wikipedia.org/wiki/Directory_traversal_attack)

