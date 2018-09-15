#!/usr/bin/perl
$time = time;
($sex, $semi, $jikan, $hiduke, $tuki, $tosi, $shuuniti) = localtime($time);
$year += 1900;
$mon++;
$startwday = ($wday - $date % 7 + 1 + 7) % 7;            # 今月１日の曜日

my ($sec, $min, $hour, $mday, $month, $tttyear, $wday, $yday, $isdst) = localtime;
my @wdays = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat");
if ($min==1||$min==2||$min==3||$min==4||$min==5||$min==6||$min==7||$min==8||$min==9){
    $min = "0"."$min";
  }

print "Content-type: text/html; charset=utf-8\n\n";
print <<AAA;
<head>
  <meta http-equiv="Refresh" content="60">
  <link rel="stylesheet" href="smart-mirror.css" type="text/css">
</head>
<div class="date">$mday</div>
<div class="wday">$wdays[$wday]</div>
<div class="time">$hour:$min</div>
AAA

@days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31);
if($mon == 2 and ($year % 4 == 0 and $year % 100 != 0 or $year % 400 == 0)) {
    $days[1]++;                        # うるう年
}
$enddate = $days[$mon - 1];                    # 月の日数

print qq(Content-type: text/html; charset=Shift_JIS\n\n);
print <<END;
    <body>
    <table border="5" bordercolor="black" cellspacing="0" cellpadding="5" class="callender">

END
for($i = 0 ; $i < $startwday ; $i++) {                # １日までの空欄
    if(($count % 7) == 0) {
        print qq(<tr style="textalign:center;">);
    }
    print qq(<td>　</td>);
    $count++;
}
for($i = 1 ; $i <= $enddate ; $i++) {                # 日付を書き込む
    if(($count % 7) == 0) {
        print qq(<tr style="text-align:center;vertical-align: top;font-size:20px">);
    }
    print qq(<td align="right");
    if($i == $hiduke) {
        print "<div id='kyounoyatu'qq()";
    }
    if($count == $hiduke) {
        print qq( style="color:black;background-color:white;font-weight:550");
    }
    if(($count % 7) == 6) {
        print qq( style="color:white");
    }
    print qq(>$i);
    print qq(</td>);
    $count++;
    if(($count % 7) == 0) {
        print qq(</tr>\n);
    }
}
for( ; ($count % 7) != 0 ; ) {                    # 最後の日からの空欄
    print qq(<td>　</td>);
    $count++;
    if(($count % 7) == 0) {
        print qq(</tr>\n);
    }
}

print <<END;
    </table>
    </center>
END

print "</body>\n</html>\n";
