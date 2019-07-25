#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2019-07-22 20:16:55






def move(n, a, b, c):
	if n == 1:
		print(a, '--->', c)
	else:
		move(n-1, a, c, b)
		print( a,'--->', c)
		move(n-1, b, a, c)

	print(move(3, a, b, c))
