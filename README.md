<h2>Validate meteo.gr forecasts</h2>

<p>
	Sometimes you don't know which weather site to trust. With this script you can calculate how accurate is a site, at this script I use meteo.gr <br>
	It downloads meteorological data from the meteo.gr and a Davis Weather station wich is placed in the city I would like to know the forecast. After that it will present the percent of success the meteo site had. 
</p>

<p>
	The meteo.gr dosn't provide any API so for the data download is used the <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">Beautiful Soup</a> lib. <br>
	Do not trust this script for long term data collection because it is based on web scraping technique. If any of the sites, in the future, change their structure the data collection will fail.  
</p>

<hr>

<h3>Installation and use</h3>
<p>
	In order to use the script, you have to use python3 and install the requirements. Some info about data download is saved to a file called info.log
</p>

```python
:~$ pip3 install -r requirements.txt
```

<p>
	After install just run the script once:
</p>

```python
:~$ python3 src/main.py
```

<p>
	Or assign the task to a cron job
</p>
TODO:
<ul>
	<li>Fix negative temperatures</li>
	<li>Optimize code</li>
</ul>
