Twitter contributions calendar
==============================

Like Github does it for its `contributions calendar <https://help.github.com/articles/viewing-contributions-on-your-profile-page/#contributions-calendar>`_, this tool displays a user's tweets in a dynamic calendar using the awesome `Cal-Heatmap <https://github.com/wa0x6e/cal-heatmap>`_ library:

.. image:: https://raw.githubusercontent.com/ncrocfer/twitter-calendar/master/calendar.png
    :alt: Twitter contributions calendar
    :width: 700
    :height: 282
    :align: center

Usage
-----

It's a simple script to launch, so I don't create the :code:`setup.py` file. To use it :

.. code-block:: bash

    $ git clone https://github.com/ncrocfer/twitter-calendar.git
    $ cd twitter-calendar
    $ pip install -r requirements.txt

Create a new `Twitter app <https://apps.twitter.com/>`_ and fill in the :code:`CONSUMER_KEY`, :code:`CONSUMER_SECRET`, :code:`ACCESS_KEY` and :code:`ACCESS_SECRET` variables. Then you can get the tweets specifying the user's account :

.. code-block:: bash

    $ python twitter-calendar.py -u ncrocfer
    [*] 399 tweets downloaded
    [*] 598 tweets downloaded
    ...

You can now copy the generated :code:`tweets.json` and :code:`index.html` files in your web root directory and see the results :)

Notes
-----

- Due to a limitation `imposed <https://dev.twitter.com/rest/reference/get/statuses/user_timeline>`_ by Twitter, this script can only return up to **3,200** of a user's most recent Tweets.
- It is a simple script for now, but many improvements are possible (for example the script can be placed in a CRON job, or it could be a real web app with the help of Flask or Django). I will look to do this in the future.
