from scrapy import cmdline

# command = "scrapy crawl likes -L INFO"
command = "scrapy crawl article -L INFO"

cmdline.execute(command.split())
