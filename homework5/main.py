#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import cgi
from google.appengine.api import users
import webapp2


#MAIN_PAGE_HTML = """\
#<html>
  #<body>
    
  #</body>
#</html>
#"""

class Root(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<form action="/test" method="post">\nPlease input <i>EINGLISH TWO</i> words!\n<br><input type=text name="word1"><br><input type=text name=word2><br><div><input type=submit value=TRANSMISSION></div></form>')
   


class WordShuffle(webapp2.RequestHandler):
    def post(self):
        str1 = self.request.get('word1')
        str2 = self.request.get('word2')

        len1 = len(str1)
        len2 = len(str2)

        if len1 <= len2: # str1 <= str2
            len_min = len1
        else: len_min = len2 # str2 < str1

        
        str3 = ''

        for num in range(0, len_min*2):
            if num % 2 == 0: # num is even
                str3 += str1[num/2]
            else: # num is odd
                str3 += str2[num/2]

        num = len_min
        if len_min < len2: # str1 < str2
            while num < len2:
                str3 += str2[num]
                num += 1
        elif len_min < len1:
            while num < len1:
                str3 += str1[num]
                num += 1
                
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1> answer is %s <h1>' % str3)

app = webapp2.WSGIApplication([
    ('/', Root),
    ('/test', WordShuffle),
], debug=True)
