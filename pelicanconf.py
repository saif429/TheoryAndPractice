#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kyle Cranmer'
SITENAME = u'Theory And Practice'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU =False
MENUITEMS = (
			('About','/index.html'),
			('Research','/pages/Research.html'),
			('Projects','/pages/projects.html'),
			('Media & Outreach','/pages/in-the-news.html'),)


LINKS =  (('My group', 'http://physics.nyu.edu/experimentalparticle/'),
          ('CCPP','http://cosmo.nyu.edu/'),
          ('CDS','http://cds.nyu.edu/'),
          ('DIANA','http://diana-hep.org/'),
          ('MSDSE','http://msdse.org'),
          ('DASPOS','http://daspos.org/'),
          )


'''
# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
		  ('Quantum Diaries', 'http://www.quantumdiaries.org/'),
#		  #('Me @ Quantum Diaries','http://www.quantumdiaries.org/author/kyle-cranmer/'),
		  ('Not Even Wrong','http://www.math.columbia.edu/~woit/wordpress/'),
		  ('Cocktail Party Physics','http://twistedphysics.typepad.com/cocktail_party_physics/'),
		  ('Résonaances','http://resonaances.blogspot.com/'),
		  ('Matt Strassler','http://profmattstrassler.com/'),
#		  #('Life as a physicist','http://gordonwatts.wordpress.com/'),
		  ('Tommaso Dorigo','http://www.science20.com/physics'),
#		  #('Cosmic Variance','http://blogs.discovermagazine.com/cosmicvariance/'),
#		  #('Collider Blog','http://muon.wordpress.com/'),
		  ('Symmetry Breaking','http://www.symmetrymagazine.org/breaking'),
		  ('INSPIRE','http://blog.inspirehep.net/'),
		  ('Data Pub','http://datapub.cdlib.org/'),
		  ('Hogg’s Research','http://hoggresearch.blogspot.com/'),)
'''

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/kylecranmer'),
          ('github', 'http://github.com/cranmer'),
          ('linkedin','http://www.linkedin.com/in/kylecranmer'),
          ('youtube','https://www.youtube.com/channel/UCKl2VoIJiPYp3QhuK22b7xQ'),
          ('figshare','http://figshare.com/authors/Kyle%20Cranmer/432748'),
          ('ImpactStory','https://impactstory.org/u/0000-0002-5769-7094'))

#          ('flickr','http://www.flickr.com/photos/hoonynoo/'),
#          ('google+','https://plus.google.com/106689822196584540592/posts'),


CC_LICENSE="CC-BY"

DEFAULT_PAGINATION = 6

#use URLs that match old wordpress site
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

# comments
DISQUS_SITENAME="theoryandpractice"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

####################################################
# Additions 
STATIC_PATHS = ['images', 'downloads', 'downloads/notebooks',
                'downloads/files','downloads/code', 'favicon.png']

READERS = {'html': None}


CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
  'liquid_tags.youtube', 'tag_cloud',
  'render_math', 
  'pelican_javascript',
  'liquid_tags.include_code', 
  'i18n_subsites',
  'pelican-ipynb.liquid' ,'liquid_tags.literal'] 
#  'liquid_tags.notebook','liquid_tags.literal'] 

#


#  'liquid_tags.notebook'

#, 'liquid_tags.thebe']

THEME = 'pelican-bootstrap3'
JINJA_EXTENSIONS = ['jinja2.ext.i18n']


#THEME = 'notmyidea'
PYGMENTS_STYLE='default'
#PYGMENTS_STYLE='friendly'
#THEME = '../pelican-bootstrap3'
#THEME = '/Users/cranmer/virtualenvs/pelican/lib/python2.7/site-packages/pelican/themes/pelican-bootstrap3'
# This requires Pelican 3.3+

#For pelican-ootstrap3
BOOTSTRAP_THEME='simplex'
BOOTSTRAP_THEME='yeti'
BOOTSTRAP_THEME='superhero' #nice but, background doesn't work well with code as is
BOOTSTRAP_THEME='cosmo' #used for T&P through 2016
BOOTSTRAP_THEME='flatly' #looks good, some color
#BOOTSTRAP_THEME='journal' #also looks good, more B&W
#BOOTSTRAP_THEME='readable' 

#BOOTSTRAP_THEME='paper'
DISPLAY_BREADCRUMBS=False
BOOTSTRAP_NAVBAR_INVERSE=False
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True

TAG_CLOUD_STEPS = 4
TAG_CLOUD_BADGE = True  
DISPLAY_TAGS_ON_SIDEBAR=True
TAG_CLOUD_MAX_ITEMS=25
DISPLAY_TAGS_INLINE=True
HIDE_SIDEBAR=False


#ABOUT_ME="I'm a professor at NYU interested in particle physics, open science, data science, and science communication to the broader public."
#AVATAR='/images/kyle-andys-party-miras-photo.jpg'
AVATAR=None
ABOUT_ME=None
#TWITTER_WIDGET_ID='353505377641447424'
TWITTER_WIDGET_ID=''
#GITHUB_USER='cranmer'
#GITHUB_REPO_COUNT=True
#GITHUB_SKIP_FORK=True
#GITHUB_SHOW_USER_LINK=True
ADDTHIS_PROFILE='ra-5332e76b5340f5f3'

GOOGLE_ANALYTICS='UA-3337202-1'
#TWITTER_CARDS='False' 


#INDEX_SAVE_AS = 'index.html'

#the deault _nb_header is changing 
#fonts etc. of rest of notmyidea and pelican-bootstrap3 themes
#looks ok in notmyidea, but no style at all in bootstrap3

#This souldn't be necessary with updated pelican-bootstrap3
#EXTRA_HEADER = open('_nb_header_minimal.html').read().decode('utf-8')
#EXTRA_HEADER = open('extra_header_minimal.html').read().decode('utf-8')
#EXTRA_HEADER = '' #need to flush
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

#DISQUS Code
'''
    <div id="disqus_thread"></div>
    <script type="text/javascript">
        /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
        var disqus_shortname = 'theoryandpractice'; // required: replace example with your forum shortname

        /* * * DON'T EDIT BELOW THIS LINE * * */
        (function() {
            var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
            dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
        })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
    <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>
'''

