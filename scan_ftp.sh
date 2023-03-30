#!/bin/sh

#ftp1信息
1_ftp_server=xxxxxx
1_ftp_user=xxxxx
1_ftp_passwd=xxxxx
#ftp2信息
2_ftp_server=xxxxxx
2_ftp_user=xxxxxx
2_ftp_passwd=xxxxxx

today=`date +"%Y-%m-%d"`
scan_time=`date +"%Y-%m-%d %H:%M:%S"`

num_18_dir=`curl -l -s ftp://${2_ftp_server}/18/ -u "${2_ftp_user}:${2_ftp_passwd}" |grep ${today} |wc -l`

if [ $num_18_dir -eq 0 ];then
        eval num_18="当天目录不存在"
elif [ $num_18_dir -eq 1 ];then
        eval num_18=`curl -s ftp://${2_ftp_server}/18/${today}/ -u "${2_ftp_user}:${2_ftp_passwd}"  |grep txt | wc -l |tail -n1`
fi



for i in 2 7 8 ;do
dir_status=`curl -l -s ftp://${1_ftp_server}/idc_home/${i}/ -u "${1_ftp_user}:${1_ftp_passwd}" |grep ${today} |wc -l `
if [ $dir_status -eq 0 ];then
        eval num_${i}="当天目录不存在"
elif [ $dir_status -eq 1 ];then
        eval num_${i}=`curl -s ftp://${1_ftp_server}/idc_home/${i}/${today}/ -u "${1_ftp_user}:${1_ftp_passwd}"  |grep txt | wc -l |tail -n1`
fi

done

mkdir -p /home/at_omd/scan_ftp/
printf "%-20s %-10s %-10s\n" 扫描时间  $scan_time    >> /home/at_omd/scan_ftp/${today}.txt
printf "%-20s %-10s %-10s\n" 日期    目录   文件数量  >> /home/at_omd/scan_ftp/${today}.txt
printf "%-20s %-10s %-10s\n" $today 2    ${num_2}     >> /home/at_omd/scan_ftp/${today}.txt
printf "%-20s %-10s %-10s\n" $today 7    ${num_7}     >> /home/at_omd/scan_ftp/${today}.txt
printf "%-20s %-10s %-10s\n" $today 8    ${num_8}     >> /home/at_omd/scan_ftp/${today}.txt
printf "%-20s %-10s %-10s\n" $today 18   ${num_18}    >> /home/at_omd/scan_ftp/${today}.txt

cat /home/at_omd/scan_ftp/${today}.txt
