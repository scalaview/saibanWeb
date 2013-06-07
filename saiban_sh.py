#!/usr/bin/python
# -*- coding: UTF-8 -*-

import web
import saiban_secondHand

urls = (
    '/.*' , 'Index',
)


render = web.template.render('templates')

app = web.application(urls, globals())


class Index:
	def GET(self):
		posts = saiban_secondHand.saiban()
		return render.index(posts)

if __name__ == '__main__':
	app.run()