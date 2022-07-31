import pywhatkit
import wikipedia

#for youtube search
def yt(query):
    try:
        op = ""
        if 'for' in query:
            result = query.find('for')
            op = query[result+3:]
        elif 'about' in query:
            result = query.find('about')
            op = query[result+5:]
        elif 'youtube' in query:
            result = query.find('youtube')
            op = query[result+7:]
        elif 'play' in query:
            result = query.find('play')
            op = query[result+4:]
        elif 'song' in query:
            result = query.find('song')
            op = query[result+4:]
        elif 'video' in query:
            result = query.find('video')
            op = query[result+5:]
        if op != "":
            pywhatkit.playonyt(op)
            return(1)
    except Exception as e:
        return (0)

#for google search
def gs(query):
    try:
        if 'for' in query:
            result = query.find('for')
            op = query[result+3:]
        elif 'about' in query:
            result = query.find('about')
            op = query[result+5:]
        elif 'is' in query:
            result = query.find('is')
            op = query[result+2:]
        elif 'google' in query:
            result = query.find('google')
            op = query[result+6:]
        else:
            op = query
        if op != "":
            pywhatkit.search(op)
            return(1)
    except Exception as e:
        return(0)

#for wikipedia
def wiki(query):
    try:
        if 'for' in query:
            result = query.find('for')
            query =query.replace(query[0:result+3], "")
        elif 'about' in query:
            result = query.find('about')
            query = query.replace(query[0:result+5],"")
        elif 'describe' in query:
            result = query.find('describe')
            query = query.replace(query[0:result+7],"")
        elif 'what is' in query:
            result = query.find('what is')
            query = query.replace(query[0:result+6],"")
        if query != "":
            wikipedia.summary(query, sentences=2)
            results = wikipedia.summary(query, sentences=2)
            return (results)
    except Exception:
        return(0)

#for short information about anything
def wikiopen(query):
    result = query.find('for')
    op = query[result+3:]
    if op != "":
        results1 = wikipedia.page(op).url
        results2 = wikipedia.summary(op, sentences=3)
        return (results1,results2)
    else:
        return("")

# for shutdown and cancel shutdown
def cancelsd():
    pywhatkit.cancelShutdown()
    return
def sd():
    pywhatkit.shutdown(time=60)
    return