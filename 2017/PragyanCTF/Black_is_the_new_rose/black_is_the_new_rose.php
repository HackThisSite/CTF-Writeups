<?php
// author: mooph
//
// first opened in VIM, there's a comment at the end of the file saying something about bash noobs, ignored...
// then there's a hint on website, that we should look for black
// then analysis of the image, there's just a few black lines
// then scripting..., I found out there's only a few black pixels per line
// then to array
// then to hex
// then hex to ascii in a browser
// the output of this script must be deciphered using Atbash cipher, thank you Blackfisk <3
$img=imagecreatefrompng("black_is_the_new_rose.png");
$res=[];
$kk=0;
for(;$kk<658;){
	$res[$kk]=0;
	++$kk;
}
$iii=0;
$xx=0;
$yy=0;
for(;$yy<658;){
	for(;$xx<1213;){
		$rgb=imagecolorat($img,$xx,$yy);
		$col=imagecolorsforindex($img,$rgb);
		if($col["red"]===0&&$col["green"]===0&&$col["blue"]===0){
			++$res[$yy];
		}
		++$iii;
		++$xx;
	}
	$xx=0;
	++$yy;
}
//print_r($res);
//echo "<br/><br/><br/><br/>";
$fus=array();
$ooo=0;
foreach($res as $rr){
	if($rr===0){
		continue;
	}
	$fus[$ooo]=$rr;
	++$ooo;
	//echo $rr;

}
//print_r($fus);
$haa=array();
$ppp=0;
foreach($fus as $boo){
	$haa[$ppp]=$boo;
	if($boo===10){
		$haa[$ppp]="a";
	}
	if($boo===11){
		$haa[$ppp]="b";
	}
	if($boo===12){
		$haa[$ppp]="c";
	}
	if($boo===13){
		$haa[$ppp]="d";
	}
	if($boo===14){
		$haa[$ppp]="e";
	}
	if($boo===15){
		$haa[$ppp]="f";
	}
	++$ppp;
}
//print_r($haa);
$qqq=0;
for(;$qqq<count($haa);){
	echo "&#x".$haa[$qqq].$haa[$qqq+1].";";
	++$qqq;
	++$qqq;
}
?>
