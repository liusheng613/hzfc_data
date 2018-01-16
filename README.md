# hzfc_data
## 简介：
- 利用scrapy+selenium+phantjs实现抓取杭州房产网数据
- 由于http://www.hzfc.gov.cn/scxx/ 数据是通过图片展示，所以抓取的是图片
- 数据分为总库存信息，新房成交信息，二手房成交信息，都是用当前日期做为前缀，文件存储到当前文件夹下的images文件夹下