# Shard

This condition is based on the one written by [Victor Vrantchan](https://github.com/whitby/mac-scripts/tree/master/munki_condition_shard). It will return a number between 1 and 100 based on the machine's serial number. This allows you to use something like the following to limit a software rollout:

``` xml
<key>installable_condition</key>
<string>shard &lt;= 25</string>
```

You can also explicitly opt out of sharding by placing a file at ``/usr/local/shard/production`` or explicitly opt into sharding by placing a file at ``/usr/local/shard/testing`` (useful for VIP machines and test machines respectively).