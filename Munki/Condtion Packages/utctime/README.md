# UTC Time

This condition will return the current time in UTC and the current UNIX timestamp. This can be useful when you need to enable a piece of software for release at the same time regardless of where the machine is located:

``` xml
<key>installable_condition</key>
<string>timestamp &lt;= 1450013911</string>
```