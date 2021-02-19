from bs4 import BeautifulSoup

def get_page_data(response):
    candidate = ''
    status = ''
    stop_loss = ''
    soup = BeautifulSoup(response)
    candidate_status = soup.find('span', {'class':'btn-group mb-20'})
    list_tag = []
    for i in candidate_status:
        if i=='\n':
            continue
        list_tag.append(i)
    candidate = list_tag[0].get_text().replace('\n','')
    status = list_tag[1].get_text().replace('\n','')
    if soup.find('span', {'class':'font-weight-400 float-right'}):
        stop_loss = soup.find('span', {'class':'font-weight-400 float-right'}).get_text()
    else:
        stop_loss = soup.find('b').get_text()
    stop_loss = stop_loss.replace('\n', '')
    next_3_months = soup.find_all('p', {'class':'text-justified'})[1].get_text()
    return {
        'candidate': candidate,
        'status': status,
        'stop_loss': stop_loss,
        'next_3_months': next_3_months
    }


response = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimal-ui">
<meta name="author" content="StockInvest.us">
<meta name="google-site-verification" content="m4hiBkvCxNQafkCRAhewzdiP7-EzN-UurLUAyMJjc4s" />
<meta id="site_root" content="site-root" name="site-root" data-root="https://stockinvest.us">
<meta name="theme-color" content="#FFFFFF" />
<title>Should You Buy CFFN Stock?</title>
<meta name="description" content="Check if CFFN has a Buy or Sell Evaluation. CFFN Stock Price (NASDAQ), Score, Forecast, Predictions, and Capitol Federal Financial News.">
<link rel="apple-touch-icon" sizes="57x57" href="https://stockinvest.us/assets/img/icons/apple-icon-57x57.png?v=3161">
<link rel="apple-touch-icon" sizes="60x60" href="https://stockinvest.us/assets/img/icons/apple-icon-60x60.png?v=3161">
<link rel="apple-touch-icon" sizes="72x72" href="https://stockinvest.us/assets/img/icons/apple-icon-72x72.png?v=3161">
<link rel="apple-touch-icon" sizes="76x76" href="https://stockinvest.us/assets/img/icons/apple-icon-76x76.png?v=3161">
<link rel="apple-touch-icon" sizes="114x114" href="https://stockinvest.us/assets/img/icons/apple-icon-114x114.png?v=3161">
<link rel="apple-touch-icon" sizes="120x120" href="https://stockinvest.us/assets/img/icons/apple-icon-120x120.png?v=3161">
<link rel="apple-touch-icon" sizes="144x144" href="https://stockinvest.us/assets/img/icons/apple-icon-144x144.png?v=3161">
<link rel="apple-touch-icon" sizes="152x152" href="https://stockinvest.us/assets/img/icons/apple-icon-152x152.png?v=3161">
<link rel="apple-touch-icon" sizes="180x180" href="https://stockinvest.us/assets/img/icons/apple-icon-180x180.png?v=3161">
<link rel="icon" type="image/png" sizes="192x192" href="https://stockinvest.us/assets/img/icons/android-icon-192x192.png?v=3161">
<link rel="icon" type="image/png" sizes="32x32" href="https://stockinvest.us/assets/img/icons/favicon-32x32.png?v=3161">
<link rel="icon" type="image/png" sizes="96x96" href="https://stockinvest.us/assets/img/icons/favicon-96x96.png?v=3161">
<link rel="icon" type="image/png" sizes="16x16" href="https://stockinvest.us/assets/img/icons/favicon-16x16.png?v=3161">
<link rel="manifest" href="/manifest.json">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="msapplication-TileImage" content="https://stockinvest.us/assets/img/icons/ms-icon-144x144.png?v=3161">
<meta name="theme-color" content="#ffffff">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="stylesheet" href="https://stockinvest.us/assets/css/addtohomescreen.css?v=3161">
<script src="https://stockinvest.us/assets/js/addtohomescreen.js?v=3161"></script>
<link rel='preload' href='/fonts/vendor/@fortawesome/fontawesome-free/webfa-solid-900.woff2?f6121be597a72928f54e7ab5b95512a1' as='font' type='font/woff2' crossorigin />
<link rel='preload' href='/fonts/vendor/@fortawesome/fontawesome-free/webfa-regular-400.woff2?9efb86976bd53e159166c12365f61e25' as='font' type='font/woff2' crossorigin />
<link rel='preload' href='/fonts/web-icons.woff2?3ed7c2762ffa97fb77e6cde88842c72f' as='font' type='font/woff2' crossorigin />
<link rel='preload' href='/fonts/material-design.woff2?a4d31128b633bc0b1cc1f18a34fb3851' as='font' type='font/woff2' crossorigin />
<link rel="stylesheet" href="https://stockinvest.us/css/app.css?v=3161">
<link rel="manifest" href="/manifest.json">
<link rel="canonical" href="https://stockinvest.us/stock/CFFN" />
<meta property="og:url" content="http://stockinvest.us/stock/CFFN" />
<meta property="og:type" content="website" />
<meta property="og:title" content="Should You Buy CFFN Stock?" />
<meta property="og:description" content="Check if CFFN has a Buy or Sell Evaluation. CFFN Stock Price (NASDAQ), Score, Forecast, Predictions, and Capitol Federal Financial News." />
<meta property="og:image" content="https://stockinvest.us/chart/2021/2/17/CFFN/main/3?mediumType=facebook" />
<meta name="ez_sub" content="1">
<script>
    dataLayer = [];
    dataLayer.push({"visitorType":"authenticated","visitorSubscribed":"subscribed","stockExchange":"NASDAQ"});
</script>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
                new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
                j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
                'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer','GTM-TVXV45B');</script>


<script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

    ga('create', 'UA-72227847-1', 'auto');
    ga('send', 'pageview');
</script>

<script>
        window.IC_drop_adhesion = 1;
</script>
<!--[if lt IE 9]>
<script src="https://stockinvest.us/assets/global/vendor/html5shiv/html5shiv.min.js?v=3161"></script>
<![endif]-->
<!--[if lt IE 10]>
<script src="https://stockinvest.us/assets/global/vendor/media-match/media.match.min.js?v=3161"></script>
<script src="https://stockinvest.us/assets/global/vendor/respond/respond.min.js?v=3161"></script>
<script src="https://stockinvest.us/assets/global/vendor/asscroll/jquery-asScroll.min.js?v=3161"></script>
<![endif]-->
<script src="https://cdn.onesignal.com/sdks/OneSignalSDK.js" async=""></script>
<script>
        window.OneSignal = window.OneSignal || [];
        OneSignal.push(function() {
            OneSignal.init({
                appId: "dc16ae21-dc34-43a4-a7ac-ae0c7e8c6949",
            });
        });
    </script>
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [{
    "@type": "ListItem",
    "position": 1,
    "name": "All Stocks",
    "item": "https://stockinvest.us/list"
  },{
    "@type": "ListItem",
    "position": 2,
    "name": "NASDAQ",
    "item": "https://stockinvest.us/list?exchanges=NASDAQ"
  },{
    "@type": "ListItem",
    "position": 3,
    "name": "CFFN",
    "item": "https://stockinvest.us/stock/CFFN"
  }]
}
</script>
</head>
<body class="site-navbar-small has-right-navbar has-right-navbar of-x-hidden menubar-mobile">
<script src="https://script.tapfiliate.com/tapfiliate.js" async></script>
<script>
    function getQueryParams() {
        var assoc  = {};
        var decode = function (s) { return decodeURIComponent( s.replace(/\+/g, " ")); };
        var queryString = location.search.substring(1);
        var keyValues = queryString.split('&');

        for(var i in keyValues) {
            var key = keyValues[i].toString().split('=');
            if (key.length > 1) {
                assoc[decode(key[0])] = decode(key[1]);
            }
        }

        return assoc;
    };

    (function(t,a,p){t.TapfiliateObject=a;t[a]=t[a]||function(){
        (t[a].q=t[a].q||[]).push(arguments)}})(window,'tap');

    var params = getQueryParams();

    tap('create', '7987-9b3b13');

    if (params.st == 'Completed') {
        var amt = params.amt || 1;
        var tx = params.tx || null;
        tap('conversion', tx,  amt);
    } else {
        tap('detect');
    }
</script>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TVXV45B"
                      height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

<script>
    /* <![CDATA[ */
    var google_conversion_id = 917783172;
    var google_custom_params = window.google_tag_params;
    var google_remarketing_only = true;
    /* ]]> */
</script>
<script src="//platform-api.sharethis.com/js/sharethis.js#property=5c5c2b3f6dbc680011d2b4f5&product=inline-share-buttons"></script><!--[if lt IE 8]>
<p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="https://browsehappy.com/" rel="noopener">upgrade
    your browser</a> to improve your experience.</p>
<![endif]-->
<div id="app-nav-bar" class="site-navbar navbar navbar-default navbar-fixed-top navbar-mega " role="navigation">
<div class="st-site-navbar-container">
<div class="navbar-header">
<button id="back-button" type="button" class="btn btn-icon btn-default float-left ml-10 mt-12 hide" onclick="history.back(-1)"><i class="fas fa-arrow-left"></i></button>
<button id="mobile-sidebar-switch" type="button" class="navbar-toggler hamburger hamburger-close navbar-toggler-left hided" data-toggle="menubar">
<span class="sr-only">Toggle navigation</span>
<span class="hamburger-bar"></span>
</button>
<button id="navbar-collapse-switch" type="button" class="navbar-toggler collapsed p-0" data-target="#site-navbar-right-collapse" data-toggle="collapse-right">
<span class="avatar avatar-xs avatar-online">
<img id="navProfilePicture" src="https://stockinvest.us/storage/user/avatars/41a87e1c8a1dba5babbdb1d1bfb7a391.jpg" alt="Ehab Elkady">
<i></i>
</span>
</button>
<div class="navbar-brand navbar-brand-center site-gridmenu-toggle hidden-xs-down" data-toggle="gridmenu">
<a href="https://stockinvest.us">
<img class="navbar-brand-logo" src="https://stockinvest.us/assets/img/general/stockinvest-logo-header.jpg?v=3161" title="StockInvest.us" alt="StockInvest.us">
</a>
</div>
<div class="navbar-brand navbar-brand-center site-gridmenu-toggle hidden-sm-up text-center" data-toggle="gridmenu">
<a href="https://stockinvest.us">
<img class="navbar-brand-logo" src="https://stockinvest.us/assets/img/general/stockinvest-logo-header.jpg?v=3161" title="StockInvest.us" alt="StockInvest.us">
</a>
</div>
<button id="mobile-search-magnifier" type="button" class="navbar-toggler collapsed" data-target="#site-navbar-search" data-toggle="collapse">
<span class="sr-only">Toggle Search</span>
<i style="font-size: 22px; margin-top: 1px" class="black icon md-search" aria-hidden="true"></i>
</button>
</div>
<div class="navbar-container container-fluid">

<div class="collapse navbar-collapse navbar-collapse-toolbar" id="site-navbar-collapse">

<ul class="nav navbar-toolbar navbar-left navbar-toolbar-left">
<li class="text-nowrap nav-item hidden-float" id="toggleMenubar" style="display: none;">
<a class="nav-link" data-toggle="menubar" href="#" role="button">
<i class="icon hamburger hamburger-arrow-left">
<span class="sr-only">Toggle menubar</span>
<span class="hamburger-bar"></span>
</i>
</a>
</li>
</ul>
<ul id="header-search-toolbar" class="nav navbar-toolbar">
<li class="text-nowrap nav-item hidden-float">
<div class="collapse navbar-search navbar-left">
<form class="navbar-form form-inline p-0 pr-10" role="search" method="GET" action="https://stockinvest.us/search">
<div class="input-search">
<input type="text" v-model="string" @input="searchTicker" name="query" class="form-control" placeholder="AAPL or Apple" autocomplete="off">
<button type="button" class="input-search-btn" aria-label="Search">
<i class="icon md-search" aria-hidden="true"></i>
</button>
</div>
</form>
<ticker-search-landing :keyword="string" :tickers="results" :show="showResults" :margintop="'-14px'"></ticker-search-landing>
</div>
</li>
</ul>

<ul class="nav navbar-toolbar">
<li class="text-nowrap nav-item dropdown dropdown-mega">
<a class="btn btn-default pl-10 pr-10" data-toggle="dropdown" href="#" aria-expanded="false" id="toggleSignals">
<i class="fas fa-lightbulb main-icon-color" aria-hidden="true"></i> <span class="hidden-icons-header-down">Trading Ideas</span> <i class="fas fa-caret-down hidden-xs-down"></i>
</a>
<div class="dropdown-menu" role="menu">

<div class="mega-content">
<div class="row">
<div class="col-sm-6 col-lg-4">
<h5 class="mt-0">Buy</h5>
<ul class="list-icons">
<li class="text-nowrap ">
<i class="fa fa-square green-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/buy/top100"> Top Buy Candidates</a>
</li>
<li class="text-nowrap ">
<i class="fas fa-running green-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/runners"> Possible Runners</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-square green-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/double-bottom-3"> Double Bottoms</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-square green-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/pivotbottoms"> Pivot Bottoms</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-square green-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/new-signals/buy">By Score & Duration</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-square green-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/undervalued"> Undervalued List</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-star yellow-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/goldenstar"> Golden Star Short</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-star green-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/goldenstar-12"> Golden Star Long</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-star green-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/bollinger/buy"> Bollinger BreakOut</a>
</li>
<li class="text-nowrap">
<i class="fa fa-plus green-600 menu-icon" aria-hidden="true"></i>
<a class="waves-effect waves-light waves-round collapsed" data-toggle="collapse" href="#mv-buy-collapse" aria-expanded="false">
Moving Averages
</a>
</li>
</ul>
<ul class="list-icons collapse in" id="mv-buy-collapse" aria-expanded="false">
<li class="text-nowrap">
<h5>Short term</h5>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-short-buy-3"> 7 days mv</a>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-long-buy-3"> 35 days mv</a>
</li>
<li class="text-nowrap">
<h5>Medium term</h5>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-short-buy-12"> 100 days mv</a>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-long-buy-12"> 200 days mv</a>
</li>
<li class="text-nowrap">
<h5>
Short/long<sup> (Golden cross)</sup>
</h5>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-buy-shortlong-3"> 7 / 35 days</a>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-buy-shortlong-12"> 35 / 100 days</a>
</li>
</ul>
</div>
<div class="col-sm-6 col-lg-4">
<h5 class="mt-0">Sell</h5>
<ul class="list-icons">
<li class="text-nowrap ">
<i class="fa fa-square red-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/sell/top100"> Top Sell Candidates</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-square red-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/new-signals/sell">By Score & Duration</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-square red-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/double-top-3"> Double Tops</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-square red-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/pivottops"> Pivot Tops</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-square red-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/overvalued"> Overvalued List</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-square red-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/deathstar"> Death Star</a>
</li>
<li class="text-nowrap ">
<i class="fa fa-square red-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/bollinger/sell"> Bollinger BreakOut</a>
</li>
<li class="text-nowrap">
<i class="fa fa-plus red-600 menu-icon" aria-hidden="true"></i>
<a class="waves-effect waves-light waves-round collapsed" data-toggle="collapse" href="#mv-sell-collapse" aria-expanded="false">
Moving Averages
</a>
</li>
</ul>
<ul class="list-icons collapse" id="mv-sell-collapse" aria-expanded="false">
<li class="text-nowrap">
<h5>Short term</h5>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-short-sell-3"> 7 days mv</a>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-long-sell-3"> 35 days mv</a>
</li>
<li class="text-nowrap">
<h5>Medium term</h5>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-short-sell-12"> 100 days mv</a>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-long-sell-12"> 200 days mv</a>
</li>
<li class="text-nowrap">
<h5>Short/long<sup> (Golden cross)</sup></h5>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-sell-shortlong-3"> 7 / 35 days</a>
</li>
<li class="text-nowrap">
<a href="https://stockinvest.us/list/mv-sell-shortlong-12"> 35 / 100 days</a>
</li>
</ul>
</div>
<div class="col-sm-6 col-lg-4">
<h5 class="mt-0">Other</h5>
<ul class="list-icons">
<li class="text-nowrap ">
<i class="fa fa-list menu-icon blue-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list"> Company List</a>
</li>
<li class="text-nowrap ">
<i class="fas fa-chart-pie menu-icon blue-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/sectors"> Sectors</a>
</li>
<li class="text-nowrap ">
<i class="fas fa-circle-notch fa-spin fa-1x fa-fw orange-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/rsi14">RSI 14</a>
</li>
<li class="text-nowrap ">
<i class="fas fa-circle-notch fa-spin fa-1x fa-fw orange-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/rsi21"> RSI 21</a>
</li>
<li class="text-nowrap ">
<i class="fas fa-chart-line menu-icon green-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/trending"> Trending</a>
</li>
<li class="text-nowrap ">
<i class="fas fa-dollar-sign menu-icon blue-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/pennystocks"> Penny Stocks</a>
</li>
 <li class="text-nowrap ">
<i class="fa fa-square orange-600 menu-icon" aria-hidden="true"></i>
<a href="https://stockinvest.us/list/hold/top100"> Top 100 Hold</a>
</li>
</ul>
</div>
</div>
<div class="text-center mt-10">
<a class="btn btn-default btn-outline pl-10 pr-10" href="https://stockinvest.us/list/breakout-stocks/latest" id="toggleMarket"><i class="fas fa-rocket main-icon-color"></i> Possible Breakout Stocks
</a>
<a class="btn btn-default btn-outline pl-10 pr-10" href="https://stockinvest.us/hausse/hausse" id="toggleMarket"><i class="fas fa-temperature-low main-icon-color"></i> Market Status
</a>
<a class="btn btn-default btn-outline m-auto" href="https://stockinvest.us/query/build">
<i class="fa fa-list main-icon-color" aria-hidden="true"></i> Ultimate List Builder
</a>
</div>
</div>
</div>
</li>
<li class="text-nowrap nav-item">
<a class="btn btn-default pl-10 pr-10" href="https://stockinvest.us/podcast" id="togglePodcast">
<i class="fas fa-podcast main-icon-color"></i> <span class="hidden-icons-header-down spec-shrink">Podcast </span></a>
</li>
<li class="text-nowrap nav-item">
<a class="btn btn-md pl-10 pr-10 btn-discord mr-0" href="https://discord.gg/TdDBjMm" target="_blank" rel="noreferrer">
<i class="fab fa-discord"></i> <span class="hidden-icons-header-down spec-shrink">Stock Chat</span></a>
</li>
</ul>

<ul class="nav navbar-toolbar navbar-right navbar-toolbar-right">
<li class="text-nowrap nav-item">
<a class="btn btn-default pl-10 pr-10" href="https://stockinvest.us/list/buy/top100" id="toggleTopStocks"><i class="fa fa-chart-line main-icon-color"></i> <span class="hidden-icons-header-down spec-shrink">Top Stocks</span></a>
</li>
<li class="text-nowrap nav-item">
<a class="btn btn-default pl-10 pr-10" href="https://stockinvest.us/predictions" id="togglePredictions">
<i class="fa fa-bullseye main-icon-color"></i>
<span class="hidden-icons-header-down spec-shrink">
Predictions
</span>
</a>
</li>
<li class="text-nowrap nav-item">
<a class="btn btn-default pl-10 pr-10" href="https://stockinvest.us/portfolios" id="togglePortfolios">
<i class="fa fa-suitcase main-icon-color"></i> <span class="hidden-icons-header-down spec-shrink">Portfolios</span>
</a>
</li>
<li class="text-nowrap nav-item">
<exchanges-dropdown>
<button type="button" class="btn btn-default pl-10 pr-10 exchange-button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
<i class="fas fa-globe-americas main-icon-color"></i> <span class="hidden-icons-header-down spec-shrink">Exchanges </span><i class="fas fa-caret-down hidden-xs-down"></i>
</button>
</exchanges-dropdown>
</li>
<li class="text-nowrap nav-item dropdown notification-dropdown" id="notifications">
<a class="nav-link pl-10 pr-10" data-toggle="dropdown" href="#" title="Notifications" aria-expanded="false" role="button" @click="changeNotificationStatus">
<i class="icon md-notifications main-icon-color" aria-hidden="true"></i>
<span v-cloak v-show="not_seen" class="badge badge-pill badge-danger up notification-badge">{{ not_seen }}</span>
</a>
<div class="dropdown-menu dropdown-menu-right dropdown-menu-media force-right notification-data" role="menu">
<div class="dropdown-menu-header">
<h5>NOTIFICATIONS</h5>
<span v-cloak v-show="not_seen" class="badge badge-round badge-danger notification-badge-inside">New notifications: {{ not_seen }}</span>
</div>
<div class="list-group">
<div data-role="container">
<notifications></notifications>
</div>
</div>
</div>
</li>
<li class="nav-item login-dropdown dropdown">
<a class="nav-link navbar-avatar mt-0" data-toggle="dropdown" href="#" aria-expanded="false" role="button">
<span class="avatar avatar-online">
<img id="navProfilePicture" src="https://stockinvest.us/storage/user/avatars/41a87e1c8a1dba5babbdb1d1bfb7a391.jpg" alt="Ehab Elkady">
<i></i>
</span>
</a>
<div class="dropdown-menu" role="menu" style="width: 250px">
<a class="dropdown-item" href="https://stockinvest.us/chat" role="menuitem">
<i class="fa fa-envelope mr-5" aria-hidden="true"></i> Messages
</a>
<a class="dropdown-item" href="https://stockinvest.us/profile/edit" role="menuitem">
<i class="icon md-settings" aria-hidden="true"></i> Profile Settings
</a>
<a class="dropdown-item" href="https://stockinvest.us/query/build" role="menuitem">
<i class="fa fa-list mr-5"></i> Ultimate List Builder
</a>
<a class="dropdown-item" href="https://stockinvest.us/watchlists" role="menuitem">
<i class="fa fa-eye mr-5"></i> Watchlist
</a>
<div class="dropdown-divider"></div>
<form action="https://stockinvest.us/logout" method="POST">
<input type="hidden" name="_token" value="13lJDjMvB43t850xxdL93so0CWj0UGOtalOcH5Lh">
<button class="dropdown-item" role="menuitem" type="submit"><i class="icon md-power" aria-hidden="true"></i> Logout</button>
</form>
</div>
</li> </ul>

</div>


<div class="collapse navbar-search-overlap" id="site-navbar-search">
<form role="search" method="GET" action="https://stockinvest.us/search">
<div class="form-group">
<div class="input-search">
<i class="input-search-icon md-search" aria-hidden="true"></i>
<input id="input-search-mobile" type="text" class="form-control" name="query" v-model="string" @input="searchTicker" placeholder="AAPL or Apple" autocomplete="off">
<button type="button" class="input-search-close icon md-close" data-target="#site-navbar-search" data-toggle="collapse" aria-label="Close">
</button>
</div>
</div>
</form>
<ticker-search-landing :keyword="string" :tickers="results" :show="showResults" :locked="false" :width="'100%'" :margintop="'0px'"></ticker-search-landing>
</div>

</div>
</div>
</div>
<div class="modal fade" id="popup-modal" aria-hidden="true" aria-labelledby="popup-modal" role="dialog" tabindex="-1">
<div class="modal-dialog popup-modal modal-simple modal-center mt-0">
<div class="modal-content text-center trial-color-bg">
<div class="modal-header text-center pr-20 pb-0 inline-block">
<button type="button" class="close white" data-dismiss="modal" aria-label="Close" style="position: absolute; right: 30px">
<span aria-hidden="true">×</span>
</button>
<h4 class="modal-title white text-center">NEWS: FREE TRIAL SUBSCRIPTION!</h4>
</div>
<div class="modal-body pt-0 pb-0">
<div class="row">
<div class="col-md-12 white">
<hr>
<p>We are all together in this COVID-19 pandemic. Your losses are our losses too. This is why we are offering FREE 14 days TRIAL SUBSCRIPTIONS with no further commitments.</p>
<p>Let's make money!</p>
<a id="trialPopupButton" href="https://stockinvest.us/order?sref=popup_covid_button" class="btn btn-md bg-white trial-btn bold">Access Premium features FREE NOW!</a>
</div>
</div>
</div>
<div class="modal-footer pt-20 pb-5">
<small class="mb-0 white">Subscribed already? <strong><a href="https://stockinvest.us/login" class="white">Log in</a></strong></small>
</div>
</div>
</div>
</div><div class="site-menubar hasContestBar site-menubar-light">
<div class="st-container">
<div class="site-menubar-body">
<div>
<div>
<ul class="site-menu" data-plugin="menu">
<li class="site-menu-item" id="menu-ticker">
<span class="animsition-link">
CFFN:
</span>
</li>
<li class="site-menu-item active">
<a class="animsition-link" href="https://stockinvest.us/stock/CFFN">
<i class="site-menu-icon fa fa-chart-bar"></i>
<span class="site-menu-title">CFFN Stock</span>
</a>
</li>
<li class="site-menu-item">
<a class="animsition-link" href="https://stockinvest.us/forecast/CFFN">
<i class="site-menu-icon fas fa-bullseye"></i>
<span class="site-menu-title">Forecast</span>
</a>
</li>
<li class="site-menu-item">
<a class="animsition-link" href="https://stockinvest.us/stock/CFFN/data">
<i class="site-menu-icon fas fa-signal"></i>
<span class="site-menu-title">Data & Signals</span>
</a>
</li>
<li class="site-menu-item">
<a class="animsition-link" href="https://stockinvest.us/stock-price/CFFN">
<i class="site-menu-icon fas fa-dollar-sign"></i>
<span class="site-menu-title">Historical Prices</span>
</a>
</li>
<li class="site-menu-item">
<a class="animsition-link" href="https://stockinvest.us/earnings-report/CFFN">
<i class="site-menu-icon fas fa-user-edit"></i>
<span class="site-menu-title">Earnings Reports</span>
</a>
</li>
<li class="site-menu-item">
<a class="animsition-link" href="https://stockinvest.us/predictions/CFFN">
<i class="site-menu-icon fa fa-user-circle"></i>
<span class="site-menu-title">Predictions</span>
</a>
</li>
<li class="site-menu-item">
<a class="animsition-link" href="https://stockinvest.us/signal-statistics/CFFN">
<i class="site-menu-icon fa fa-chart-area"></i>
<span class="site-menu-title">Statistics</span>
</a>
</li>
<li class="site-menu-item">
<a class="animsition-link" href="https://stockinvest.us/news/CFFN">
<i class="site-menu-icon fa fa-rss"></i>
<span class="site-menu-title">News</span>
</a>
</li>
<li class="site-menu-item">
<a class="animsition-link" href="https://stockinvest.us/info/CFFN">
<i class="site-menu-icon fa fa-building"></i>
<span class="site-menu-title">Profile</span>
</a>
</li>
</ul>
 </div>
</div>
</div>
</div>
</div>
<div id="app-mobile-sidebar" class="site-menubar site-menubar-right site-menubar-light hidden-md-up">
<div class="site-menubar-body scrollable-vertical of-y">
<div>
<div>
<ul class="site-menu" data-plugin="menu">
<li class="dropdown site-menu-item has-sub mt-10">
<a data-toggle="dropdown" href="javascript:void(0)" data-dropdown-toggle="false">
<i class="site-menu-icon fa fa-user" aria-hidden="true"></i>
<span class="site-menu-title">Profile</span>
<span class="site-menu-arrow"></span>
</a>
<div class="dropdown-menu">
<div class="site-menu-scroll-wrap is-list">
<div>
<div>
<ul class="site-menu-sub site-menu-normal-list">
<li class="site-menu-item">
<a href="https://stockinvest.us/chat">
<i class="site-menu-icon fa fa-envelope" aria-hidden="true"></i> Messages
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/profile/edit">
<i class="site-menu-icon md-settings" aria-hidden="true"></i> Profile Settings
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/query/build">
<i class="site-menu-icon fa fa-list"></i> Ultimate List Builder
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/watchlists">
<i class="site-menu-icon fa fa-eye"></i> Watchlists
</a>
</li>
<li class="site-menubar-divider"></li>
<li class="site-menu-item">
<div class="m-15 ml-20">
<form action="https://stockinvest.us/logout" method="POST">
<input type="hidden" name="_token" value="13lJDjMvB43t850xxdL93so0CWj0UGOtalOcH5Lh">
<button class="dropdown-item" role="menuitem" type="submit"><i class="icon md-power" aria-hidden="true"></i> Logout</button>
</form>
</div>
</li>
</ul>
</div>
</div>
</div>
 </div>
</li>
<li class="site-menubar-divider"></li>
<li class="dropdown site-menu-item has-sub">
<a data-toggle="dropdown" href="javascript:void(0)" data-dropdown-toggle="false">
<i class="site-menu-icon fas fa-podcast main-icon-color" aria-hidden="true"></i>
<span class="site-menu-title">Podcast</span>
<span class="site-menu-arrow"></span>
</a>
<div class="dropdown-menu">
<div class="site-menu-scroll-wrap is-list">
<div>
<div>
<ul class="site-menu-sub site-menu-normal-list">
<li class="site-menu-item">
<a rel="nofollow" href="http://hyperurl.co/stockinvest-spotify">
<img class="site-menu-icon lazyload" data-src="https://stockinvest.us/assets/img/brand-icons/spotify.png?v=3161" alt="Listen to our stock podcast from Spotify" style="margin-top: -2px"> Spotify
</a>
</li>
<li class="site-menu-item">
<a rel="nofollow" href="http://hyperurl.co/stockinvest-google">
<img class="site-menu-icon lazyload" data-src="https://stockinvest.us/assets/img/brand-icons/google-podcasts.png?v=3161" alt="Listen to our stock podcast from Google Podcast" style="margin-top: -2px"> Google Podcasts
</a>
</li>
<li class="site-menu-item">
<a rel="nofollow" href="http://hyperurl.co/stockinvest-apple">
<img class="site-menu-icon lazyload" data-src="https://stockinvest.us/assets/img/brand-icons/apple-podcasts.png?v=3161" alt="Listen to our stock podcast from Apple Podcasts" style="margin-top: -2px"> Apple Podcasts
</a>
</li>
<li class="site-menu-item">
<a rel="nofollow" href="http://hyperurl.co/stockinvest-breaker">
<img class="site-menu-icon lazyload" data-src="https://stockinvest.us/assets/img/brand-icons/breaker-podcasts.png?v=3161" alt="Listen to our stock podcast from Breaker" style="margin-top: -2px"> Breaker
</a>
</li>
<li class="site-menu-item">
<a rel="nofollow" href="http://hyperurl.co/stockinvest-overcast">
<img class="site-menu-icon lazyload" data-src="https://stockinvest.us/assets/img/brand-icons/overcast-podcasts.svg?v=3161" alt="Listen to our stock podcast from Overcast" style="margin-left: -2px; margin-top: -2px"> Overcast
</a>
</li>
<li class="site-menu-item">
<a rel="nofollow" href="http://hyperurl.co/stockinvest-pocket">
<img class="site-menu-icon lazyload" data-src="https://stockinvest.us/assets/img/brand-icons/pocketcasts.png?v=3161" alt="Listen to our stock podcast from Pocket Casts" style="margin-top: -2px"> Pocket Casts
</a>
</li>
<li class="site-menu-item">
<a rel="nofollow" href="http://hyperurl.co/stockinvest-radio">
<img class="site-menu-icon lazyload" data-src="https://stockinvest.us/assets/img/brand-icons/radiopublic-podcasts.png?v=3161" alt="Listen to our stock podcast from Radio Public" style="margin-top: -2px"> Radio Public
</a>
</li>
<li class="site-menu-item">
<a rel="nofollow" href="https://anchor.fm/stockinvest">
<img class="site-menu-icon lazyload" data-src="https://stockinvest.us/assets/img/brand-icons/anchor-podcasts.png?v=3161" alt="Listen to our stock podcast from Anchor" style="margin-top: -2px"> Anchor
</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/buy/top100">
<i class="site-menu-icon fa fa-chart-line main-icon-color"></i> Top Stocks
</a>
</li>
<li class="dropdown site-menu-item has-sub">
<a data-toggle="dropdown" href="javascript:void(0)" data-dropdown-toggle="false">
<i class="site-menu-icon fas fa-lightbulb main-icon-color" aria-hidden="true"></i>
<span class="site-menu-title">Trading Ideas</span>
<span class="site-menu-arrow"></span>
</a>
<div class="dropdown-menu">
<div class="site-menu-scroll-wrap is-list">
<div>
<div>
<ul class="site-menu-sub site-menu-normal-list">
<li class="site-menu-item has-sub">
<a href="javascript:void(0)" class="">
<i class="site-menu-icon wb-graph-up color-green" aria-hidden="true"></i>
<span class="site-menu-title">Buy Candidates</span>
<span class="site-menu-arrow"></span>
</a>
<ul class="site-menu-sub">
<li class="site-menu-item">
<a href="https://stockinvest.us/list/buy/top100">
<i class="site-menu-icon fa fa-square color-green" aria-hidden="true"></i>
Top Buy Candidates
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/runners">
<i class="site-menu-icon fas fa-running color-green" aria-hidden="true"></i>
Possible Runners
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/double-bottom-3">
<i class="site-menu-icon fa fa-square color-green" aria-hidden="true"></i>
Double Bottoms
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/pivotbottoms">
<i class="site-menu-icon fa fa-square color-green" aria-hidden="true"></i>
Pivot Bottoms
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/undervalued">
<i class="site-menu-icon fa fa-square color-green" aria-hidden="true"></i>
Undervalued List
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/goldenstar">
<i class="site-menu-icon fa fa-star yellow-600" aria-hidden="true"></i>
Golden Star Short Term
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/goldenstar-12">
<i class="site-menu-icon fa fa-star yellow-600" aria-hidden="true"></i>
Golden Star Medium Term
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/bollinger/buy">
<i class="site-menu-icon fa fa-star color-green" aria-hidden="true"></i>
Bollinger BreakOut
</a>
</li>
</ul>
</li>
<li class="site-menu-item has-sub">
<a href="javascript:void(0)" class="">
<i class="site-menu-icon wb-graph-down color-red" aria-hidden="true"></i>
<span class="site-menu-title">Sell Candidates</span>
<span class="site-menu-arrow"></span>
</a>
<ul class="site-menu-sub">
<li class="site-menu-item">
<a href="https://stockinvest.us/list/sell/top100">
<i class="site-menu-icon fa fa-square color-red" aria-hidden="true"></i>
Top Sell Candidates
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/new-signals/sell">
<i class="site-menu-icon fa fa-square color-red" aria-hidden="true"></i>
By Score & Duration
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/double-top-3">
<i class="site-menu-icon fa fa-square color-red" aria-hidden="true"></i>
Double Tops
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/pivottops">
<i class="site-menu-icon fa fa-square color-red" aria-hidden="true"></i>
Pivot Tops
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/overvalued">
<i class="site-menu-icon fa fa-square color-red" aria-hidden="true"></i>
Overvalued List
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/deathstar">
<i class="site-menu-icon fa fa-square color-red" aria-hidden="true"></i>
Death Star
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/bollinger/sell">
<i class="site-menu-icon fa fa-star color-red" aria-hidden="true"></i>
Bollinger BreakOut
</a>
</li>
</ul>
</li>
<li class="site-menu-item has-sub">
<a href="javascript:void(0)">
<i class="site-menu-icon wb-library" aria-hidden="true"></i>
<span class="site-menu-title">Other Lists</span>
<span class="site-menu-arrow"></span>
</a>
<ul class="site-menu-sub">
<li class="site-menu-item">
<a href="https://stockinvest.us/list">
<i class="site-menu-icon fa fa-list menu-icon blue-600" aria-hidden="true"></i>
Company List
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/sectors">
<i class="site-menu-icon fas fa-chart-pie menu-icon blue-600" aria-hidden="true"></i>
Sectors
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/rsi14">
<i class="site-menu-icon fas fa-circle-notch fa-spin fa-1x fa-fw orange-600" aria-hidden="true"></i>
RSI 14
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/rsi21">
<i class="site-menu-icon fas fa-circle-notch fa-spin fa-1x fa-fw orange-600" aria-hidden="true"></i>
RSI 21
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/trending">
<i class="site-menu-icon fas fa-chart-line menu-icon color-green" aria-hidden="true"></i>
Trending
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/pennystocks">
<i class="site-menu-icon fas fa-dollar-sign menu-icon blue-600" aria-hidden="true"></i>
Penny Stocks
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/hold/top100">
<i class="site-menu-icon fa fa-square orange-600" aria-hidden="true"></i>
Top 100 Hold
</a>
</li>
</ul>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/list/breakout-stocks/latest">
<i class="site-menu-icon fas fa-rocket main-icon-color" aria-hidden="true"></i>
Possible Breakout Stocks
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/hausse/hausse">
<i class="site-menu-icon fas fa-temperature-low main-icon-color" aria-hidden="true"></i>
Market Status
</a>
</li>
</ul>
</div>
</div>
</div>
</div>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/portfolios">
<i class="site-menu-icon fa fa-suitcase main-icon-color"></i> Portfolios
</a>
</li>
<li class="site-menu-item">
<a href="https://stockinvest.us/predictions">
<i class="site-menu-icon fa fa-bullseye main-icon-color"></i> Predictions
</a>
</li>
<li class="dropdown site-menu-item has-sub">
<a data-toggle="dropdown" href="javascript:void(0)" @click="dropdownLoad" data-dropdown-toggle="false">
<i class="site-menu-icon fas fa-globe-americas main-icon-color" aria-hidden="true"></i>
<span class="site-menu-title">Select Your Market</span>
<span class="site-menu-arrow"></span>
</a>
<div class="dropdown-menu">
<div class="site-menu-scroll-wrap is-list">
<div>
<div>
<ul class="site-menu-sub site-menu-normal-list">
<li v-for="(exchange, index) in exchanges" :key="index" class="site-menu-item">
<a :href="exchange.route"> {{ exchange.display_name }}</a>
</li>
</ul>
</div>
</div>
</div>
</div>
<li class="text-nowrap nav-item">
<li class="site-menu-item">
<a href="https://discord.gg/TdDBjMm" target="_blank" rel="noreferrer">
<i class="site-menu-icon fab fa-discord discord-icon-color"></i> Stock Chat
</a>
</li>
</ul>
</div>
</div>
</div>
</div>
<div class="page">
<div class="st-container">
<div class="page-content container-fluid">
<div class="row">
<div class="col-lg-9">
<div id="status_box" style="display: none">
<div class="row">
<div class="col-md-12">
<div class="alert alert-success alert-dismissible" role="alert" style="margin-top: 10px">
<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
<strong>Success!</strong><div id="status_message"></div>
</div>
</div>
</div>
</div> <div class="card card-shadow mb-10">
<div class="card-block pb-15 pt-15 pl-15-md pr-15-md " style="border: 2px #ffc107 solid; border-radius: 3px">
<div class="row">
<div class="col-sm-12 col-xs-12 text-center">
<div class="ta-header-buttons">
<next-previous-buttons symbol="CFFN" is_subscribed=""></next-previous-buttons>
</div>
</div>
</div>
<div class="ticker-header-flex-container">
<div class="ticker-header-left-content">
<h1 class="m-0 overflow-text-ellipsis ticker-heading-text pt-5 color-orange">
Capitol Federal Financial
Stock Forecast
<span class="badge badge-ticker badge-default badge-outline">NASDAQ:<a class="animsition-link" href="  https://stockinvest.us/stock/CFFN" title="CFFN is listed at NASDAQ"><strong class="bold">CFFN</strong></a></span>
</h1>
<div class="ta-realtime-price">
<ta-realtime-price-component ticker="CFFN" currency="USD" change="-0.61" closeprice="13.07" lastdate="2021-02-17"></ta-realtime-price-component>
</div>
</div>
<div class="ticker-header-right-content">
<div class="gauge pull-right exampleDynamicGauge" id="exampleDynamicGauge" data-plugin="gauge" data-value="-0.93" data-max-value="10">
<div class="badge badge-lg badge-warning" id="gauge-text"></div>
<canvas width="110" height="75"></canvas>
</div>
</div>
</div>
<div class="row">
<div class="col-md-12 no-wrap">
<div class="float-left" style="display: flex">
<div class="watchlist-button mr-5" style="float: left">
<watchlist-button :ticker_id="475">
<a class="btn btn-default btn-xs" :href="'/register'"><i class="fa fa-plus" aria-hidden="true"></i> Watchlist</a>
</watchlist-button>
</div>
<div class="dropdown display-inline pr-5">
<button type="button" class="btn btn-default dropdown-toggle btn-xs" id="reportDropdownMenu" data-toggle="dropdown" aria-expanded="false">
<i class="fa fa-bug" aria-hidden="true"></i> Report
</button>
<div class="dropdown-menu" role="menu">
<a class="dropdown-item reportable-button" role="menuitem" data-issue="1" data-tickerid="475" data-csrf="13lJDjMvB43t850xxdL93so0CWj0UGOtalOcH5Lh">
Split - Wrong Prices/Values
</a>
<a class="dropdown-item reportable-button" role="menuitem" data-issue="2" data-tickerid="475" data-csrf="13lJDjMvB43t850xxdL93so0CWj0UGOtalOcH5Lh">
Doesn't exist anymore
</a>
<a class="dropdown-item reportable-button" role="menuitem" data-issue="3" data-tickerid="475" data-csrf="13lJDjMvB43t850xxdL93so0CWj0UGOtalOcH5Lh">
Wrong Signals
</a>
</div>
</div> <a href="https://api.stocktwits.com/widgets/share" id="stocktwits-share-button"></a>
</div>
<div class="font-size-12 mt-5 pl-5 overflow-text-ellipsis text-right hidden-xs-down">
<a href="https://stockinvest.us/list?exchanges=NASDAQ" title=" NASDAQ Stock Exchange">NASDAQ Stock Exchange</a>
> <a href="https://stockinvest.us/industry/378" title=" Savings &amp; Cooperative Banks">Savings &amp; Cooperative Banks</a>
> <a href="https://stockinvest.us/sector/36" title=" Financial Services">Financial Services</a>
</div>
</div>
</div>
</div>
<script src="https://api.stocktwits.com/addon/button/share.min.js"></script>
</div>
<div class="modal fade" id="watchlistCreateModal" data-backdrop="false" tabindex="-1" role="dialog">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
<h4 class="modal-title">Create a Watchlist</h4>
</div>
<form action="https://stockinvest.us/watchlist/create" method="post">
<input type="hidden" name="_token" value="13lJDjMvB43t850xxdL93so0CWj0UGOtalOcH5Lh">
<div class="modal-body" style="max-height: 600px">
<input type="text" class="form-control" name="name" placeholder="Enter watchlists' name" required>
</div>
<div class="modal-footer">
<button class="btn btn-animate btn-animate-side btn-success" data-toggle="modal" type="submit">
<span><i class="icon md-plus" aria-hidden="true"></i>Create</span>
</button>
<button type="button" class="btn btn-animate btn-animate-side btn-default" data-dismiss="modal">
<span><i class="icon md-minus" aria-hidden="true"></i>Close</span>
</button>
</div>
</form>
</div>
</div>
</div>
<div class="sharethis-inline-share-buttons mb-10"></div>
<div class="panel panel-bordered mb-20" id="predictions">
<div class="panel-body pl-0 pr-0 pt-20 pt-10-md pb-5">
<div class="row">
<div class="col-md-9 pr-10 pl-0-md pr-15-md">
<div class="row mb-15 ml-5 mr-0 ml-15-md mr-10-md">
<div class="col-sm-5 col-xs-6 no-wrap">
<div class="btn-group">
<a class="btn btn-sm-xs  btn-primary" href="https://stockinvest.us/stock/CFFN">
3M
</a>
<a class="btn btn-sm-xs btn-outline btn-default" href="https://stockinvest.us/stock/CFFN/?chart=12">
12M
</a>
<a class="btn btn-sm-xs btn-outline btn-default" href="https://stockinvest.us/stock/CFFN/?chart=bollinger">
Bollinger
</a>
</div>
<a class="btn btn-sm btn-default hidden-md-down mr-1" target="_blank" href="https://stockinvest.us/chart/2021/2/17/CFFN/main/3?mediumType=facebook&download=1">
<i class="fa fa-download"></i>
</a>
</div>
<div class="col-sm-7 col-xs-6 text-right no-wrap pr-0 pr-5-md">
<predict-ta ref="predictTA" :score_id="30769674" :price="13.07" :ticker_id="475" :requested="0" :userprediction="0" :symbol="'CFFN'"></predict-ta>
</div>
</div>
<div @click="changePriceFromChart" id="chart_main_475" style="width: 100%; height: 75%" data-source="https://stockinvest.us/json/chart/2021/2/17/CFFN/3/main" data-price-output-el="price_input_field" data-change-percent-output-el="prediction_change_percent_output"></div>
</div>
<div class="col-md-3">
<div class="row pr-20 pl-15-md pr-15-md">
<div class="col-lg-12 pl-0 pb-10 pl-15-md pt-10-md">
<span class="inline-block hidden-sm-up font-weight-500 font-size-12 grey-800 mt-7">Wed, Feb 17, 2021</span>
<span class="btn-group w-100p">
<a class="btn btn-sm btn-secondary bg-warning w-100p" href="https://stockinvest.us/list/buy/top100">
Hold/Accumulate
</a>
<a class="btn btn-sm btn-secondary }}" href="https://stockinvest.us/list/buy/top100">
Unchanged
</a>
</span>
</div>
</div>
<div class="row pr-20 pl-15-md">
<div class="col-lg-12 pl-0 pl-15-md pr-10-md pb-5">
<div class="alert dark alert-warning alert-dismissible bg-color-orange" role="alert">
<h4>Golden Star Identified!</h4>
<p>
Golden Star is a rare signal often followed by significant gains. Get the list of all stocks with recently detected <a class="underline white" href="https://stockinvest.us/list/goldenstar">Golden Stars here</a>.
</p>
</div>
</div>
</div>
<div class="row pr-20 pl-15-md">
<div class="col-lg-12 pl-0 pl-15-md pr-10-md pb-5">
</div>
<div class="col-lg-12 pl-0 pl-15-md pr-10-md mb-5 mt-5">
<h5 class="font-size-12"><i class="fas fa-stop-circle color-red"></i> Stop-loss: <span class="font-weight-400 float-right"> $12.65 (-3.21%)</span></h5>
</div>
<div class="col-lg-12 pl-0 pl-15-md pr-10-md">
<h5 class="font-size-12"><i class="fas fa-key color-green"></i> Key Stats</h5>
<table class="table table-sm font-size-12 mb-5">
<tbody>
<tr>
<td>P/E Ratio</td>
<td class="grey-800 text-right">29.98</td>
</tr>
<tr>
<td>Beta</td>
<td class="grey-800 text-right">0.83</td>
</tr>
<tr>
<td>Trailing Dividend Rate</td>
<td class="grey-800 text-right">2.54% ($0.33)</td>
</tr>
</tbody>
</table>
</div>
</div> </div>
</div>
<div class="row m-10">
<div class="col-lg-9">
<div id="chart_rsi_475" data-source="https://stockinvest.us/json/chart/2021/2/17/CFFN/3/rsi" style="height: 130px"></div>
<small class="hidden-sm-down">
* StockInvest.us uses dynamically calculated RSI max/min levels to determine when stock is oversold or overbought based on historical behavior.
</small>
</div>
<div class="col-lg-3 text-justify">
<h5>
RSI<small>min/max</small> Values: [ <strong>25 - 75</strong> ]
</h5>
<small class="mb-0 mt-5">RSI14 is <strong>51</strong> and the stock is currently not being overbought or oversold </small>
</div>
</div>
</div>
</div>
<div class="panel panel-bordered">
<div class="panel-body text-justify pb-20">
<div class="row">
<div class="col-md-12">
<h2 class="font-size-24 mb-0 inline-block">
Capitol Federal Financial stock price down 0.6084% on Wednesday <small>(Updated on February 17, 2021)</small>
</h2>
<br>
<span class="badge badge-lg badge-warning mb-0 mt-10" style="display: inline-block;">Hold candidate since 2021-02-16</span>
<span class="mb-5 mt-10 badge badge-lg badge-danger" style="display: inline-block;">Loss -0.61%</span>
<a href="https://stockinvest.us/pdf/technical-analysis/CFFN " target="_blank" class="inline-block float-right btn-xs btn-default mt-10" style="padding: 3px 8px 3px 8px">
<i class="fa fa-file-pdf" aria-hidden="true"></i> PDF
</a> <p class="text-justified mt-15">The <strong>Capitol Federal Financial</strong> stock price fell by <span class="color-red" style="font-size: 12px"><i class="fa fa-arrow-down" aria-hidden="true"></i></span><strong class="color-red">-0.6084%</strong> on the last day (Wednesday, 17th Feb 2021) from <strong>$13.15</strong> to <strong>$13.07</strong>. During the day the stock fluctuated <strong>1.80%</strong> from a day low at <strong>$13.04</strong> to a day high of <strong>$13.28</strong>. The price has risen in 6 of the last 10 days and is up by <span class="color-green" style="font-size: 12px"><i class="fa fa-arrow-up" aria-hidden="true"></i></span><strong class="color-green">4.39%</strong> over the past 2 weeks. Volume has increased on the last day by <span class="color-green" style="font-size: 12px"><i class="fa fa-arrow-up" aria-hidden="true"></i></span><strong class="color-green">438 thousand</strong> shares but on falling prices. This may be an early warning and the risk will be increased slightly over the next couple of days. In total, <strong>982</strong> thousand shares were bought and sold for approximately <strong>$12.83</strong> million.</p>
<p class="text-justified">The stock lies in the middle of a weak rising trend in the short term and a further rise within the trend is signaled. Given the current short-term trend, the stock is expected to rise <span class="color-green" style="font-size: 12px"><i class="fa fa-arrow-up" aria-hidden="true"></i></span><strong class="color-green">3.95%</strong> during the next 3 months and, with a 90% probability hold a price between <strong>$12.89</strong> and <strong>$14.10</strong> at the end of this 3-month period.</p>
<h3 class="font-size-18 mt-0">Signals & Forecast</h3>
<p class="text-justified">The <strong>Capitol Federal Financial</strong> stock holds buy signals from both short and long-term moving averages giving a positive forecast for the stock. Also, there is a general buy signal from the relation between the two signals where the short-term average is above the long-term average. On corrections down, there will be some support from the lines at <strong>$12.88</strong> and <strong>$12.87</strong>. A breakdown below any of these levels will issue sell signals. Furthermore, there is a buy signal from the 3 months Moving Average Convergence Divergence (MACD). Some negative signals were issued as well, and these may have some influence on the near short-term development. A sell signal was issued from a pivot top point on <strong class="color-red">Tuesday, February 16, 2021</strong>, and so far it has fallen -0.6084%. Further fall is indicated until a new bottom pivot has been found. Volume rose on falling prices yesterday. This may be an early warning and the stock should be followed more closely. The stock had a <b>Golden Star Signal*</b> on <b>Friday, February 12, 2021</b> in the short-term chart.<br><br>* <i><b>Golden Star Signal*</b> is when the short-term moving average, the long-term moving average, and price line meet in a special combination. This combination is very rare and often followed by long and strong gains for the stock in question.</i></p>
<div class="row display-flex">
<div class="col-xs-12 col-sm-6 col-md-4 col-lg-4">
<div class="offer offer-radius offer-warning">
<div class="shape">
<div class="shape-text">
Buy
</div>
</div>
<div class="offer-content">
<span class="badge badge-secondary">Special Signal Notification</span>
 <h4 class="mt-0 mb-5">
Golden Star
</h4>
<small>
The stock had a <b>Golden Star Signal*</b> on <b>Friday, February 12, 2021</b> in the short-term chart.<br><br>* <i><b>Golden Star Signal*</b> is when the short-term moving average, the long-term moving average, and price line meet in a special combination. This combination is very rare and often followed by long and strong gains for the stock in question.</i>
</small>
</div>
<a href="https://stockinvest.us/list/goldenstar" title="Link To Golden Star List">
<span class="linkSpanner"></span>
</a>
</div>
</div>
</div>
<h3 class="font-size-18 mt-0">Support, Risk & Stop-loss</h3>
<p>
<strong>Capitol Federal Financial</strong> finds support from accumulated volume at $12.70 and this level may hold a buying opportunity as an upwards reaction can be expected when the support is being tested.
</p>
<div class="hidden-md-up mb-10">
<button type="button" class="btn btn-success tooltip-success btn-xs font-size-14" data-toggle="tooltip" data-placement="bottom" data-trigger="hover" data-original-title="Support" title="">
$12.70
</button>
<i class="fa fa-arrow-left"></i>
<button type="button" class="btn btn-default btn-xs font-size-14" data-toggle="tooltip" data-placement="bottom" data-trigger="click" data-original-title="Price" title="">
$13.07
</button>
<span class="badge badge-default font-size-14"></span>
<i class="fa fa-arrow-right"></i>
<button type="button" class="btn btn-danger tooltip-danger btn-xs font-size-14" data-toggle="tooltip" data-placement="bottom" data-trigger="click" data-original-title="Resistance" title="">
$13.15
</button>
</div>
<p>
This stock is usually traded at a good volume, and with minor daily changes, the risk is considered to be low. During the last day, the stock moved <strong>$0.24 (1.80%)</strong> between high and low. For the last week, the stock has had a daily average volatility of <strong>2.45%</strong>.
</p>
<p>
</p>
<p>Our recommended stop-loss:
<b>
$12.65
(-3.21%)
</b> (This stock has low daily movements and this gives low risk. There is a sell signal from a pivot top found 1 day(s) ago.)
</p>
<h3 class="font-size-18 mt-0">Is Capitol Federal Financial stock A Buy? </h3>
<p>
<strong>Capitol Federal Financial</strong> holds several positive signals, but we still don't find these to be enough for a buy candidate. At the current level, it should be considered as a hold candidate (hold or accumulate) in this position whilst awaiting further development.
</p>
<p>
Current score:
<span class="text-warning bold">-0.930</span>
</p>
<div class="row">
<div class="col-lg-7 col-md-12">
<h4>Predicted Opening Price for Capitol Federal Financial of Thursday, February 18, 2021</h4>
<p class="mb-15">The predicted opening price is based on yesterday's movements between high, low, and the closing price.</p>
</div>
<div class="col-lg-5 col-md-12">
<table class="table text-center mb-0">
<tr>
<th>Fair opening price <span class="no-wrap">February 18, 2021</span></th>
<th>Current price</th>
</tr>
<tr>
<td class="text-center">
<span class="text-success bold">$13.13</span>
</td>
<td class="text-center">
$13.07
<span class="text-success bold">(Undervalued)</span>
</td>
</tr>
</table>
</div>
</div>
<span class="btn-group mb-20">
<a class="btn btn-sm btn-secondary bg-warning" href="https://stockinvest.us/list/buy/top100" title="Our Evaluation Of Capitol Federal Financial">
Hold/Accumulate
</a>
<a class="btn btn-sm btn-secondary" href="https://stockinvest.us/list/buy/top100" title="This Stock Is Unchanged Change Since Last Evaluation">
Unchanged
</a>
</span>
<div class="row mb-20">
<div class="col-lg-3 col-md-6">
<div class="card bg-light" style="min-height: 20rem">
<div class="card-header text-center">
<i class="fa fa-user-tie"></i> Analyst Ratings
</div>
<div class="card-body border d-flex flex-column align-items-center">
<p class="card-text my-auto">
Piper Sandler does not see either upside or downside right now giving CFFN "Neutral" on their last update on October 29, 2020. The price target was set to <strong>$10.00 → $12.00</strong>.
</p>
</div>
</div>
</div>
<div class="col-lg-3 col-md-6">
<div class="card bg-light" style="min-height: 20rem">
<div class="card-header text-center">
<i class="fas fa-exclamation"></i> Volatility
</div>
<div class="card-body border d-flex flex-column align-items-center">
<span class="card-text my-auto">
<span class="
                                        light-green-500
                                                                                font-weight-500 mb-0" style="font-size: 2.572rem">2.45 %</span><br>
<small>Daily Average Volatility</small>
</p>
</div>
</div>
</div>
<div class="col-lg-3 col-md-6">
<div class="card bg-light" style="min-height: 20rem">
<div class="card-header text-center">
<i class="fas fa-exclamation"></i> Overall Risk
</div>
<div class="card-body border d-flex flex-column align-items-center">
<p class="card-text my-auto">
<span class="badge badge-default font-size-14 mb-5 w-100">Very High</span><br>
<span class="badge badge-default font-size-14 mb-5 w-100">High</span><br>
<span class="badge badge-default font-size-14 mb-5 w-100">Medium</span><br>
<span class="badge white bg-light-green-500 font-size-14 mb-5 w-100">Low</span><br>
<span class="badge badge-default font-size-14 mb-0 w-100">Very Low</span>
</p>
</div>
</div>
</div>
<div class="col-lg-3 col-md-6">
<div class="card bg-light" style="min-height: 20rem">
<div class="card-header text-center">
<i class="far fa-hand-paper"></i> Support & Resistance
</div>
<div class="card-body border d-flex flex-column align-items-center">
<p class="card-text my-auto">
<span class="badge badge-danger font-size-14 badge-lg mb-10 w-150">Resistance: $13.15</span><br>
<span class="badge badge-default font-size-14 mb-10 w-150">Price: $13.07</span><br>
<span class="badge badge-success font-size-14 badge-lg mb-10 w-150">Support: $12.70</span>
</p>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="ta-header-buttons">
<next-previous-buttons symbol="CFFN" is_subscribed=""></next-previous-buttons>
</div>
</div>
</div>
<div class="panel panel-bordered mb-20">
<div class="panel-body">
<div class="row">
<div class="col-lg-6">
<h3 class="font-size-24">Trading levels for CFFN</h3>
</div>
<div class="col-lg-6 mb-10">
<a style="border-radius: 4px;" class="btn btn-success btn-xs" role="button" href="https://stockinvest.us/article/accumulated_volume"><i class="fa fa-file-text-o" aria-hidden="true"> </i> Support & Resistance - Acc. volume </a>
<a style="border-radius: 4px;" class="btn btn-success btn-xs" role="button" href="https://stockinvest.us/article/what-is-stop-loss"><i class="fa fa-file-text-o" aria-hidden="true"> </i> What is stop-loss? </a>
</div>
</div>
<div class="row">
<div class="col-lg-6">
<h4>Fibonacci Support & Resistance Levels</h4>
<table class="table text-center">
<tr>
<th class="text-center"></th>
<th class="text-center">Level</th>
<th class="text-center">Price</th>
<th class="text-center">Change</th>
</tr>
<tr>
<td rowspan="3" class="v-align-middle">
<span style="font-size: 25px;" class="color-green">
<i class="fa fa-arrow-up"></i>
</span>
</td>
<td rowspan="3" class="v-align-middle">Resistance</td>
<td class="text-danger">13.36</td>
<td class="text-success">
<i class="fa fa-caret-up" aria-hidden="true"></i> 2.24
%
</td>
</tr>
<tr>
<td class="text-danger">13.27</td>
<td class="text-success">
<i class="fa fa-caret-up" aria-hidden="true"></i> 1.56
%
</td>
</tr>
<tr>
<td class="text-danger">13.22</td>
<td class="text-success">
<i class="fa fa-caret-up" aria-hidden="true"></i> 1.13
%
</td>
</tr>
<tr>
<td>Current price:</td>
<td></td>
<td><strong>13.07</strong></td>
<td></td>
</tr>
<tr>
<td rowspan="3" class="v-align-middle">
<span style="font-size: 25px" class="color-red">
<i class="fa fa-arrow-down"></i>
</span>
</td>
<td rowspan="3" class="v-align-middle">Support</td>
<td class="text-success">13.04</td>
<td class="text-danger">
<i class="fa fa-caret-down" aria-hidden="true"></i> -0.24
%
</td>
</tr>
<tr>
<td class="text-success">12.98</td>
<td class="text-danger">
<i class="fa fa-caret-down" aria-hidden="true"></i> -0.66
%
</td>
</tr>
<tr>
<td class="text-success">12.89</td>
<td class="text-danger">
<i class="fa fa-caret-down" aria-hidden="true"></i> -1.35
%
</td>
</tr>
</table>
</div>
<div class="col-lg-6">
<h4>Accumulated Volume Support & Resistance Levels</h4>
<table class="table text-center">
<tr>
<th></th>
<th>Level</th>
<th>Price</th>
<th>Chg %</th>
</tr>
<tr>
<td rowspan="3" class="v-align-middle">
<span style="font-size: 25px" class="color-green">
<i class="fa fa-arrow-up"></i>
</span>
</td>
<td rowspan="3" class="v-align-middle">Resistance</td>
<td class="text-danger">13.30</td>
<td class="text-success">
<i class="fa fa-caret-up" aria-hidden="true"></i> 1.76
%
</td>
</tr>
<tr>
<td class="text-danger">13.22</td>
<td class="text-success">
<i class="fa fa-caret-up" aria-hidden="true"></i> 1.15
%
</td>
</tr>
<tr>
<td class="text-danger">13.15</td>
<td class="text-success">
<i class="fa fa-caret-up" aria-hidden="true"></i> 0.61
%
</td>
</tr>
<tr>
<td>Current price</td>
<td></td>
<td><strong>13.07</strong></td>
<td></td>
</tr>
<tr>
<td rowspan="3" class="v-align-middle">
<span style="font-size: 25px" class="color-red">
<i class="fa fa-arrow-down"></i>
</span>
</td>
<td rowspan="3" class="v-align-middle">Support</td>
<td class="text-success">12.70</td>
<td class="text-danger">
<i class="fa fa-caret-down" aria-hidden="true"></i> -2.87%
</td>
</tr>
<tr>
<td class="text-success">12.42</td>
<td class="text-danger">
<i class="fa fa-caret-down" aria-hidden="true"></i> -4.97%
</td>
</tr>
<tr>
<td class="text-success">12.21</td>
<td class="text-danger">
<i class="fa fa-caret-down" aria-hidden="true"></i> -6.58%
</td>
</tr>
</table>
</div>
</div>
</div>
</div>
<h2 class="color-green text-center bold mt-10 mb-25 ml-5 mr-5">
<a href="https://www.subscribepage.com/stockinvest" title="Get Our Newsletter For Free" target="_blank" rel="noopener" style="text-decoration-line: underline"> Click</a> to get the best stock tips for free!
</h2>
<div id="app-visitor-ticker-suggestion" data-symbol="CFFN">
<div class="col-lg-12 text-center pb-20 hide">
<h4>Your most visited tickers:</h4>
<span v-for="(suggestedTicker, index) in suggestedTickers" :key="index" class="btn-group mr-5 mt-5 mb-5">
<a :class="'btn btn-sm btn-' + suggestedTicker.badge" :href="suggestedTicker.href">
{{ suggestedTicker.symbol }}
</a>
<a class="btn btn-sm btn-secondary" :href="suggestedTicker.href">
{{ suggestedTicker.score }}
</a>
</span>
</div>
</div> </div>
<div class="col-lg-3">
<div id="cf-country-NL"></div>
<div class="panel panel-bordered hidden-sm-down">
<div class="panel-heading"><h3 class="text-center pt-10 mb-10 mt-0">About Capitol Federal Financial</h3></div>
<div class="panel-body black pt-10 pb-20">
<p class="text-justify"><img src='https://stockinvest.us/storage/logos/capfed.com.png' align='left' width='80' class='pr-10 pt-10'> Capitol Federal Financial, Inc. operates as the holding company for Capitol Federal Savings Bank that provides various retail banking products and services in the United States. The company accepts various deposit products comprising savings accounts, money market accounts, interest-bearing and noninterest-bearing checking accounts, and certificates of deposits. It also provides various loan products, such as one- to four-family residential real ... <a href="https://stockinvest.us/info/CFFN" class="text-underline">Read more</a></p>
</div>
</div>
<div class="panel panel-bordered">
<div class="panel-body text-center black pt-20 pb-20">
<h3 class="text-center mb-10 mt-0">Golden Star <i class="fa fa-star color-orange" aria-hidden="true"></i></h3>
<table class="table table-tickers text-center black table-sm">
<tr>
<th class="text-center">
Ticker
</th>
<th class="text-center">
Date
</th>
<th class="text-center">
Price
</th>
<th class="text-center">
Change
</th>
</tr>
<tr>
<td class="">
<a href="https://stockinvest.us/list/goldenstar">
T
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
Feb 12
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
$28.80
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
<i class="fa fa-caret-up color-green" aria-hidden="true"></i>
2.67%
</a>
</td>
</tr>
<tr>
<td class="">
<a href="https://stockinvest.us/list/goldenstar">
CFFN
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
Feb 12
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
$12.82
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
<i class="fa fa-caret-up color-green" aria-hidden="true"></i>
1.95%
</a>
</td>
</tr>
<tr>
<td class="">
<a href="https://stockinvest.us/list/goldenstar">
CBB
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
Feb 12
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
$15.28
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
<i class="fa fa-caret-up color-green" aria-hidden="true"></i>
0.26%
</a>
</td>
</tr>
<tr>
<td class="">
<a href="https://stockinvest.us/list/goldenstar">
UFPT
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
Feb 12
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
$47.34
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
<i class="fa fa-caret-up color-green" aria-hidden="true"></i>
2.45%
</a>
</td>
</tr>
<tr>
<td class="">
<a href="https://stockinvest.us/list/goldenstar">
NVT
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
Feb 12
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
$23.40
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
<i class="fa fa-caret-up color-green" aria-hidden="true"></i>
4.91%
</a>
</td>
</tr>
<tr>
<td class="">
 <a href="https://stockinvest.us/list/goldenstar">
FRGAP
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
Feb 11
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
$25.15
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
<i class="fa fa-caret-up color-green" aria-hidden="true"></i>
0.64%
</a>
</td>
</tr>
<tr>
<td class="">
<a href="https://stockinvest.us/list/goldenstar">
CNP
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
Feb 11
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
$21.25
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
<i class="fa fa-caret-up color-green" aria-hidden="true"></i>
1.32%
</a>
</td>
</tr>
<tr>
<td class="">
<a href="https://stockinvest.us/list/goldenstar">
SCM
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
Feb 10
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
$10.72
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
<i class="fa fa-caret-up color-green" aria-hidden="true"></i>
4.57%
</a>
</td>
</tr>
<tr>
<td class="">
<a href="https://stockinvest.us/list/goldenstar">
CIF
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
Feb 10
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
$2.52
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
<i class="fa fa-caret-up color-green" aria-hidden="true"></i>
1.98%
</a>
</td>
</tr>
<tr>
<td class="">
<a href="https://stockinvest.us/list/goldenstar">
EUSGU
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
Feb 10
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
$10.99
</a>
</td>
<td class=" ">
<a href="https://stockinvest.us/list/goldenstar">
<i class="fa fa-caret-up color-green" aria-hidden="true"></i>
1.09%
</a>
</td>
</tr>
</table>
<a class="btn btn-default" href="https://stockinvest.us/list/goldenstar">
<i class="fa fa-list" aria-hidden="true"></i> Show entire list
</a>
</div>
</div>
<div id="ticker-news-feed-widget">
<ticker-news-feed-widget symbol="CFFN"></ticker-news-feed-widget>
</div>
<div class="panel panel-bordered">
<div class="panel-body p-20 text-center">
<h3 class="card-title"><img data-src="https://stockinvest.us/assets/img/general/logo-only.png?v=3161" class="lazyload logo-only-mini" alt="StockInvest.us" style="width: 24px; margin-right: 1px">Best Stock Tips Ever!</h3>
<p class="card-text">Did you miss out on NIO?</p>
<p class="card-text">What about Tesla?</p>
<small class="card-text">Don't miss out on the runners!</small>
<p><a href="https://www.subscribepage.com/stockinvest" class="btn btn-success">Get The StockInvest.Us Newsletter</a></p>
</div>
</div>
<div id="predictions-stream">
<prediction-streams ticker-symbol="CFFN" panel="true"></prediction-streams>
</div>
<div class="panel panel-bordered" id="anchor-fm-feed">
<div class="panel-body">
<h3><img data-src="https://stockinvest.us/assets/img/general/logo-only.png?v=3161" class="lazyload media-object logo-only-mini" alt="StockInvest.us"><span>Stock Podcast</span></h3>
<anchor-fm-feed></anchor-fm-feed>
</div>
</div>
<div class="panel panel-bordered">
<div class="panel-body text-center">
<h3>Top Fintech Company</h3>
<p class="grey-800 text-left"><img src="https://stockinvest.us/assets/img/general/stockinvest_us.png" alt="StockInvest.us" style="margin-bottom: 8px" height="18"> featured in <strong>The Global Fintech Index 2020</strong> as the top Fintech company of the country.</p>
<p class="mb-0 text-right"><a href="https://findexable.com/wp-content/uploads/2019/12/Findexable_Global-Fintech-Rankings-2020exSFA.pdf" target="_blank" rel="noopener">Full report by <img data-src="https://stockinvest.us/assets/img/general/findexable.png" class="lazyload" alt="FINDEXABLE" height="18"></a></p>
</div>
</div><div class="sharethis-inline-follow-buttons"></div><p class="text-center pt-20"><a rel="nofollow" href="https://rockitvilnius.com" target="_blank" rel="noopener"><img class="lazyload" data-src="https://stockinvest.us/assets/img/general/rockit.png" alt="ROCKIT" height="30"></a></p>
</div>
</div>
</div>
</div>
</div>
<div id="chat-bar">
<chat-widget></chat-widget>
<chat-sidebar></chat-sidebar>
<div class="site-action hidden-sm-down" id="footer-buttons">
<chat-button></chat-button>
</div>
<footer class="site-footer text-center pb-0" id="footerId">
<div class="st-container">
<div class="text-center">
<a href="https://stockinvest.us/about-us">
About
</a> |
<a href="https://stockinvest.us/blog">
Blog
</a> |
<a href="https://stockinvest.us/contact-us">
Contact
</a> |
<a href="https://stockinvest.us/article/list/faq">
Q&A
</a> |
<a href="/affiliates" target="_blank">
Affiliate Program
</a> |
<a href="https://stockinvest.us/investor-relations">
Investor Relations
</a> |
<a href="https://stockinvestus.typeform.com/to/GABB6C" target="_blank" rel="noopener">
Educational Plan
</a> |
<a href="https://stockinvest.us/disclaimer">
Disclaimer
</a> |
<a href="https://stockinvest.us/refunds">
Cancelation & Refunds Policy
</a>
|
<a href="https://www.subscribepage.com/stockinvest" target="_blank" rel="noopener">
Newsletter
</a> |
<a href="https://stockinvest.us/ccpa">
Do Not Sell My Personal Information
</a>
<p class="text-center mb-0">Real-time data provided for free by <a href="https://iextrading.com/developer" rel="noopener" target="_blank">IEX</a>. View <a href="https://iextrading.com/api-exhibit-a/" target="_blank" rel="noopener">IEX’s Terms of Use</a>.</p>
</div>
</div>
</footer>
<footer class="site-footer" style="border-top: 0 !important">
<div class="st-container">
<div class="col-lg-12">
<p class="text-center">"StockInvest.us" is a research service that provides financial data and technical analysis of publicly traded stocks.
All users should speak with their financial advisor before buying or selling any securities.
Users should not base their investment decision upon "StockInvest.us". By using the site you agree and are held
liable for your own investment decisions and agree to <a href="https://stockinvest.us/terms-of-use">
Terms of Use</a> and <a href="https://stockinvest.us/privacy-policy">Privacy Policy</a>.
<a href="https://stockinvest.us/disclaimer" class="red">Please read the full disclaimer here.</a></p> </div>
</div>
</footer>
</div>
<script>
    let ul = "1";
    let us = "{&quot;id&quot;:9506,&quot;user_id&quot;:212339,&quot;name&quot;:&quot;main&quot;,&quot;stripe_id&quot;:&quot;sub_Iy8Rrqc6EA5uzc&quot;,&quot;stripe_status&quot;:&quot;trialing&quot;,&quot;stripe_plan&quot;:&quot;recurring_1m_1&quot;,&quot;discount_item&quot;:&quot;{\&quot;id\&quot;:116,\&quot;active\&quot;:1,\&quot;global\&quot;:0,\&quot;discount_perc\&quot;:20,\&quot;valid_from\&quot;:\&quot;2020-06-07 00:01:47\&quot;,\&quot;valid_until\&quot;:\&quot;2024-06-08 00:01:51\&quot;,\&quot;promo_code\&quot;:\&quot;just_registered_83218ac34c1834c26781fe4\&quot;,\&quot;stripe_id\&quot;:\&quot;\&quot;,\&quot;created_at\&quot;:\&quot;2020-06-07 21:01:58\&quot;,\&quot;updated_at\&quot;:\&quot;2020-06-07 21:01:58\&quot;}&quot;,&quot;order_item&quot;:&quot;{\&quot;description\&quot;:\&quot;StockInvest.us monthly subscription - $19.90\&quot;,\&quot;amount\&quot;:1990,\&quot;duration\&quot;:1,\&quot;currency\&quot;:\&quot;USD\&quot;,\&quot;currency_sign\&quot;:\&quot;$\&quot;,\&quot;credit\&quot;:20,\&quot;type\&quot;:\&quot;recurring\&quot;,\&quot;item\&quot;:\&quot;recurring_1m_1\&quot;,\&quot;trial\&quot;:true,\&quot;trial_period\&quot;:14}&quot;,&quot;quantity&quot;:1,&quot;trial_ends_at&quot;:&quot;2021-03-04 13:03:41&quot;,&quot;ends_at&quot;:null,&quot;created_at&quot;:&quot;2021-02-18 13:03:43&quot;,&quot;updated_at&quot;:&quot;2021-02-18 13:03:43&quot;}"
</script>
<script src="https://stockinvest.us/assets/js/echarts.min.js?v=3161"></script>
<script src="https://stockinvest.us/assets/js/moment.js?v=3161"></script>
<script src="https://stockinvest.us/assets/js/moment-timezone.js?v=3161"></script>
<script src="https://stockinvest.us/js/chatbar.js?v=3161"></script>
<script src="https://stockinvest.us/js/prediction.js?v=3161"></script>
<script src="https://stockinvest.us/js/notification.js?v=3161"></script>
<script src="https://stockinvest.us/js/ta-realtime-price.js?v=3161"></script>
<script src="https://stockinvest.us/js/ta-next-previous-buttons.js?v=3161"></script>
<script src="https://stockinvest.us/js/watchlist-button.js?v=3161"></script>
<script src="https://stockinvest.us/js/ticker-news-feed-widget.js?v=3161"></script>
<div id="popoverHoverableChart" hidden style="overflow: hidden;">
<div class="popover-chart-container" style="width: 100%; height: 260px; overflow: hidden;">
<div id="popoverChartLocation" style="width: 100%; height: 100%; overflow: hidden;"></div>
</div>
</div>
<div id="popoverPredictionExplanation" hidden>
<div class="prediction_explanation_popover">
<div id="popoverPredictionExplanationLocation">
<div class="widget text-center">
Click the <a class="btn bg-orange-400 btn-xs white" style="z-index: 0">Predict</a> button to answer the prediction request. Test your skills and become famous. Best predictor for any stock is listed at the stock pages.
</div>
</div>
</div>
</div>
<div id="popoverRequestedUsers" hidden>
<div class="requested_users_popover">
<div id="popoverRequestLocation"></div>
</div>
</div>
<div id="popoverPredictedUsers" hidden>
<div class="requested_users_popover">
<div id="popoverPredictedLocation"></div>
</div>
</div>
<div id="popoverMacdChart" hidden>
<div class="macd-chart-container" style="padding-top: 20px; padding-bottom: 10px; width: 100%; height: 100%;">
<div id="popoverMacdLocation" style="width: 100%; height: 100px"></div>
</div>
</div>
<div id="popoverBollingerChart" hidden>
<div class="bollinger-chart-container" style="padding-top: 20px; padding-bottom: 10px; width: 100%; height: 100%;">
<div id="popoverBollingerLocation" style="width: 100%; height: 100px"></div>
</div>
</div>
<div id="popoverWatchlistChart" hidden>
<div class="popover-watchlist-container" style="width: 100%; height: 250px;">
<div id="popoverWatchlistLocation" style="width: 100%; height: 100%"></div>
</div>
</div>
<div id="popoverTrialFeatures" hidden>
<div class="trial_features_popover" style="width: 100%; height: 295px;">
<div id="popoverTrialFeaturesLocation" style="width: 100%; height: 295px;"></div>
</div>
</div>
<script src="https://stockinvest.us/js/app_page_bottom.js?v=3161"></script>
<script>
    function refreshReCaptchaV3(fieldId,action){
        return new Promise(function (resolve, reject) {
            grecaptcha.ready(function () {
                grecaptcha.execute(window['client'+fieldId], {
                    action: action
                }).then(resolve);
            });
        });
    }

    function getReCaptchaV3Response(fieldId){
        return grecaptcha.getResponse(window['client'+fieldId])
    }
</script>
<script>
    let show_login_dropdown = false;
</script>
<script>
    if (window.matchMedia('(display-mode: standalone)').matches) {
        $('#back-button').attr('style','display: block !important');
        $('#mobile-sidebar-switch').attr('style','margin-left: 0px !important');
    }
</script> <script async src="https://api.stocktwits.com/addon/button/share.min.js"></script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"si":10,"rayId":"623a11210ed01eb1","version":"2021.2.0"}'></script>
</body>
</html>
'''
print(get_page_data(response))