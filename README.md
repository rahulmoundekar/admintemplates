# admintemplates
### What is Template Inheritance?
  Static files improve the performance of the website. Developers use it more efficiently with template inheritance method 
  and it is one of Django’s key features.

  The basic concept is that: We define the common parts of a webpage, such as navigation bars and About section. 
  All these parts are essentially HTML and some static files. Majority of webpages will contain similar sections.

  The problem is that when there are lots of webpages, the modification becomes complex. 
  Suppose we want to modify the About section. Then, the developer will have to change the code on every single page. 
  That will lead to chaos and will definitely generate bugs.

  Django templating solves this problem, by inheritance. 
  It provides us with the modularity of developing different sections of a webpage. 
  Like we can define a base template, which contains nav bars and About section. 
  Then inherit this page and just add the unique part in other webpages.

### Collectstatic command

  This command is very useful when the website is in production state. When this command is executed, 
  Django performs these operations:

  It looks for static files in all the directories listed in STATICFILES_DIRS
  The static-files are then copied and saved in STATIC_ROOT directory.
  When the server is requested for static content, it will fetch a file from STATIC_ROOT.
  And, that file will have its URL modified with STATC_URL.
