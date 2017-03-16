FCT TV — Crawlers
=================

<img src="http://imgur.com/ZoDtdrI.png" width="200px">

## General info

**FCT TV** is an idea for a campus' TV at FCT-UNL, which will satisfy the student's needs and raise the awareness for the interesting events that are offered every day.

Our solution has 4 different parts:

* Information crawlers (this one)
* <a href="https://github.com/gdiasdasilva/FCT-TV-WebServer" target="_blank">Ruby on Rails Web server</a>
* <a href="https://github.com/gdiasdasilva/FCT-TV-TVClient" target="_blank">TV Client</a>
* iPhone app

## Description

This component is based on three python scripts that crawl specific information from FCT-UNL's official website in a daily basis:
* Meal
* Dates and students for academic presentations (PhD, Master thesis...)
* News

The technology used was <a href="http://scrapy.org" target="_blank">Scrapy</a>.

To run each crawler, change to its root directory and type:
* `scrapy crawl spider_name -o outputFileName.json -t json`

##### Example
Crawl the news from FCT-UNL's website:
* `scrapy crawl noticias -o myoutput.json -t json`

## Authors

* Gonçalo Dias da Silva
* João Francisco Pinto
* Rui Carvalho
