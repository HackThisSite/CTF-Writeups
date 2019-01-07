# Blind

>Solves: 57

>Hacking blind: http://35.207.132.47:82

>Flag is at /flag

>Difficulty estimate: Medium

## Disclaimer: Credit goes to @dgeex, he solved this challenge before I did 
## Analysis

Site discovers its source code.

```
<?php
  function __autoload($cls) {
    include $cls;
  }

  class Black {
    public function __construct($string, $default, $keyword, $store) {
      if ($string) ini_set("highlight.string", "#0d0d0d");
      if ($default) ini_set("highlight.default", "#0d0d0d");
      if ($keyword) ini_set("highlight.keyword", "#0d0d0d");

      if ($store) {
            setcookie('theme', "Black-".$string."-".$default."-".$keyword, 0, '/');
      }
    }
  }

  class Green {
    public function __construct($string, $default, $keyword, $store) {
      if ($string) ini_set("highlight.string", "#00fb00");
      if ($default) ini_set("highlight.default", "#00fb00");
      if ($keyword) ini_set("highlight.keyword", "#00fb00");

      if ($store) {
            setcookie('theme', "Green-".$string."-".$default."-".$keyword, 0, '/');
      }
    }
  }

  if ($_=@$_GET['theme']) {
    if (in_array($_, ["Black", "Green"])) {
      if (@class_exists($_)) {
        ($string = @$_GET['string']) || $string = false;
        ($default = @$_GET['default']) || $default = false;
        ($keyword = @$_GET['keyword']) || $keyword = false;

        new $_($string, $default, $keyword, @$_GET['store']);
      }
    }
  } else if ($_=@$_COOKIE['theme']) {
    $args = explode('-', $_);
    if (class_exists($args[0])) {
      new $args[0]($args[1], $args[2], $args[3], '');
    }
  } else if ($_=@$_GET['info']) {
    phpinfo();
  }

  highlight_file(__FILE__);
```


Line of particular interest to us is ```new $args[0]($args[1], $args[2], $args[3], '');```

We can create instance of any included class. It'd be great if one of them allowed us to read /flag file

## Solution

We're looking for already included class with __construct that has minimally 4 arguments and allows for fourth one to be empty.
[This page](http://php.net/manual/en/reserved.classes.php) listed some already included classes , sadly none of them were usable for reading file.
However text says something interesting:
>Miscellaneous extensions define other classes which are described in their reference. 

Notice that code has functionality to call phpinfo(), which if we do lists among other things various "Miscellaneous extensions" ;)
At this point it becomes game of finding right class, I wasted quite a bit of time playing around SPL classes with no success.

Eventually I found (again shouts to @dgeex who did it before I did :) ) SimpleXMLElement class whose __construct looks like this:
```php
final public SimpleXMLElement::__construct ( string $data [, int $options = 0 [, bool $data_is_url = FALSE [, string $ns = "" [, bool $is_prefix = FALSE ]]]] 
```
So if we make GET request with theme cookie set to SimpleXMLElement-/flag-0-True
we get a lot of warnings since /flag is not valid xml file but we also get a flag!

35c3_even_a_blind_squirrel_finds_a_nut_now_and_then in


