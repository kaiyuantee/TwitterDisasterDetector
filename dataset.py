import pandas as pd
import re

dd = {
    "$" : " dollar ",
    "€" : " euro ",
    "4ao" : "for adults only",
    "a.m" : "before midday",
    "a3" : "anytime anywhere anyplace",
    "aamof" : "as a matter of fact",
    "acct" : "account",
    "adih" : "another day in hell",
    "afaic" : "as far as i am concerned",
    "afaict" : "as far as i can tell",
    "afaik" : "as far as i know",
    "afair" : "as far as i remember",
    "afk" : "away from keyboard",
    "app" : "application",
    "approx" : "approximately",
    "apps" : "applications",
    "asap" : "as soon as possible",
    "asl" : "age, sex, location",
    "atk" : "at the keyboard",
    "ave." : "avenue",
    "aymm" : "are you my mother",
    "ayor" : "at your own risk",
    "b&b" : "bed and breakfast",
    "b+b" : "bed and breakfast",
    "b.c" : "before christ",
    "b2b" : "business to business",
    "b2c" : "business to customer",
    "b4" : "before",
    "b4n" : "bye for now",
    "b@u" : "back at you",
    "bae" : "before anyone else",
    "bak" : "back at keyboard",
    "bbbg" : "bye bye be good",
    "bbc" : "british broadcasting corporation",
    "bbias" : "be back in a second",
    "bbl" : "be back later",
    "bbs" : "be back soon",
    "be4" : "before",
    "bfn" : "bye for now",
    "blvd" : "boulevard",
    "bout" : "about",
    "brb" : "be right back",
    "bros" : "brothers",
    "brt" : "be right there",
    "bsaaw" : "big smile and a wink",
    "btw" : "by the way",
    "bwl" : "bursting with laughter",
    "c/o" : "care of",
    "cet" : "central european time",
    "cf" : "compare",
    "cia" : "central intelligence agency",
    "csl" : "can not stop laughing",
    "cu" : "see you",
    "cul8r" : "see you later",
    "cv" : "curriculum vitae",
    "cwot" : "complete waste of time",
    "cya" : "see you",
    "cyt" : "see you tomorrow",
    "dae" : "does anyone else",
    "dbmib" : "do not bother me i am busy",
    "diy" : "do it yourself",
    "dm" : "direct message",
    "dwh" : "during work hours",
    "e123" : "easy as one two three",
    "eet" : "eastern european time",
    "eg" : "example",
    "embm" : "early morning business meeting",
    "encl" : "enclosed",
    "encl." : "enclosed",
    "etc" : "and so on",
    "faq" : "frequently asked questions",
    "fawc" : "for anyone who cares",
    "fb" : "facebook",
    "fc" : "fingers crossed",
    "fig" : "figure",
    "fimh" : "forever in my heart",
    "ft." : "feet",
    "ft" : "featuring",
    "ftl" : "for the loss",
    "ftw" : "for the win",
    "fwiw" : "for what it is worth",
    "fyi" : "for your information",
    "g9" : "genius",
    "gahoy" : "get a hold of yourself",
    "gal" : "get a life",
    "gcse" : "general certificate of secondary education",
    "gfn" : "gone for now",
    "gg" : "good game",
    "gl" : "good luck",
    "glhf" : "good luck have fun",
    "gmt" : "greenwich mean time",
    "gmta" : "great minds think alike",
    "gn" : "good night",
    "g.o.a.t" : "greatest of all time",
    "goat" : "greatest of all time",
    "goi" : "get over it",
    "gps" : "global positioning system",
    "gr8" : "great",
    "gratz" : "congratulations",
    "gyal" : "girl",
    "h&c" : "hot and cold",
    "hp" : "horsepower",
    "hr" : "hour",
    "hrh" : "his royal highness",
    "ht" : "height",
    "ibrb" : "i will be right back",
    "ic" : "i see",
    "icq" : "i seek you",
    "icymi" : "in case you missed it",
    "idc" : "i do not care",
    "idgadf" : "i do not give a damn fuck",
    "idgaf" : "i do not give a fuck",
    "idk" : "i do not know",
    "ie" : "that is",
    "i.e" : "that is",
    "ifyp" : "i feel your pain",
    "IG" : "instagram",
    "iirc" : "if i remember correctly",
    "ilu" : "i love you",
    "ily" : "i love you",
    "imho" : "in my humble opinion",
    "imo" : "in my opinion",
    "imu" : "i miss you",
    "iow" : "in other words",
    "irl" : "in real life",
    "j4f" : "just for fun",
    "jic" : "just in case",
    "jk" : "just kidding",
    "jsyk" : "just so you know",
    "l8r" : "later",
    "lb" : "pound",
    "lbs" : "pounds",
    "ldr" : "long distance relationship",
    "lmao" : "laugh my ass off",
    "lmfao" : "laugh my fucking ass off",
    "lol" : "laughing out loud",
    "ltd" : "limited",
    "ltns" : "long time no see",
    "m8" : "mate",
    "mf" : "motherfucker",
    "mfs" : "motherfuckers",
    "mfw" : "my face when",
    "mofo" : "motherfucker",
    "mph" : "miles per hour",
    "mr" : "mister",
    "mrw" : "my reaction when",
    "ms" : "miss",
    "mte" : "my thoughts exactly",
    "nagi" : "not a good idea",
    "nbc" : "national broadcasting company",
    "nbd" : "not big deal",
    "nfs" : "not for sale",
    "ngl" : "not going to lie",
    "nhs" : "national health service",
    "nrn" : "no reply necessary",
    "nsfl" : "not safe for life",
    "nsfw" : "not safe for work",
    "nth" : "nice to have",
    "nvr" : "never",
    "nyc" : "new york city",
    "oc" : "original content",
    "og" : "original",
    "ohp" : "overhead projector",
    "oic" : "oh i see",
    "omdb" : "over my dead body",
    "omg" : "oh my god",
    "omw" : "on my way",
    "p.a" : "per annum",
    "p.m" : "after midday",
    "pm" : "prime minister",
    "poc" : "people of color",
    "pov" : "point of view",
    "pp" : "pages",
    "ppl" : "people",
    "prw" : "parents are watching",
    "ps" : "postscript",
    "pt" : "point",
    "ptb" : "please text back",
    "pto" : "please turn over",
    "qpsa" : "what happens", #"que pasa",
    "ratchet" : "rude",
    "rbtl" : "read between the lines",
    "rlrt" : "real life retweet",
    "rofl" : "rolling on the floor laughing",
    "roflol" : "rolling on the floor laughing out loud",
    "rotflmao" : "rolling on the floor laughing my ass off",
    "rt" : "retweet",
    "ruok" : "are you ok",
    "sfw" : "safe for work",
    "sk8" : "skate",
    "smh" : "shake my head",
    "sq" : "square",
    "srsly" : "seriously",
    "ssdd" : "same stuff different day",
    "tbh" : "to be honest",
    "tbs" : "tablespooful",
    "tbsp" : "tablespooful",
    "tfw" : "that feeling when",
    "thks" : "thank you",
    "tho" : "though",
    "thx" : "thank you",
    "tia" : "thanks in advance",
    "til" : "today i learned",
    "tl;dr" : "too long i did not read",
    "tldr" : "too long i did not read",
    "tmb" : "tweet me back",
    "tntl" : "trying not to laugh",
    "ttyl" : "talk to you later",
    "u" : "you",
    "u2" : "you too",
    "u4e" : "yours for ever",
    "utc" : "coordinated universal time",
    "w/" : "with",
    "w/o" : "without",
    "w8" : "wait",
    "wassup" : "what is up",
    "wb" : "welcome back",
    "wtf" : "what the fuck",
    "wtg" : "way to go",
    "wtpa" : "where the party at",
    "wuf" : "where are you from",
    "wuzup" : "what is up",
    "wywh" : "wish you were here",
    "yd" : "yard",
    "ygtr" : "you got that right",
    "ynk" : "you never know",
    "zzz" : "sleeping bored and tired"

}


def read_dataset():
    cleaner = Cleaner()
    train = cleaner.process_text(df=pd.read_csv('train.csv'))
    test = cleaner.process_text(df=pd.read_csv('test.csv'))
    sub = pd.read_csv('submission.csv')
    return train, test, sub


class Cleaner:

    @staticmethod
    def abbra(text):
        text = re.sub(r'\w+', lambda a: dd.get(a.group(), a.group()), text)
        return text

    @staticmethod
    def remove_emoji(text):
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

    @staticmethod
    def clean(tweet):

        # Urls
        tweet = re.sub(r"https?:\/\/t.co\/[A-Za-z0-9]+", "", tweet)
        tweet = re.sub(r'\n', ' ', tweet)
        tweet = re.sub('\s+', ' ', tweet).strip()  # leading tail

        # Words with punctuations and special characters
        punctuations = '@#!?+&*[]-%.:/();$=><|{}^' + "'`"
        for p in punctuations:
            tweet = tweet.replace(p, '')

            # Special characters
        tweet = re.sub(r"\x89Û_", "", tweet)
        tweet = re.sub(r"\x89ÛÒ", "", tweet)
        tweet = re.sub(r"\x89ÛÓ", "", tweet)
        tweet = re.sub(r"\x89ÛÏWhen", "When", tweet)
        tweet = re.sub(r"\x89ÛÏ", "", tweet)
        tweet = re.sub(r"China\x89Ûªs", "China's", tweet)
        tweet = re.sub(r"let\x89Ûªs", "let's", tweet)
        tweet = re.sub(r"\x89Û÷", "", tweet)
        tweet = re.sub(r"\x89Ûª", "", tweet)
        tweet = re.sub(r"\x89Û\x9d", "", tweet)
        tweet = re.sub(r"å_", "", tweet)
        tweet = re.sub(r"\x89Û¢", "", tweet)
        tweet = re.sub(r"\x89Û¢åÊ", "", tweet)
        tweet = re.sub(r"fromåÊwounds", "from wounds", tweet)
        tweet = re.sub(r"åÊ", "", tweet)
        tweet = re.sub(r"åÈ", "", tweet)
        tweet = re.sub(r"JapÌ_n", "Japan", tweet)
        tweet = re.sub(r"Ì©", "e", tweet)
        tweet = re.sub(r"å¨", "", tweet)
        tweet = re.sub(r"SuruÌ¤", "Suruc", tweet)
        tweet = re.sub(r"åÇ", "", tweet)
        tweet = re.sub(r"å£3million", "3 million", tweet)
        tweet = re.sub(r"åÀ", "", tweet)

        # Contractions
        tweet = re.sub(r"he's", "he is", tweet)
        tweet = re.sub(r"there's", "there is", tweet)
        tweet = re.sub(r"We're", "We are", tweet)
        tweet = re.sub(r"That's", "That is", tweet)
        tweet = re.sub(r"won't", "will not", tweet)
        tweet = re.sub(r"they're", "they are", tweet)
        tweet = re.sub(r"Can't", "Cannot", tweet)
        tweet = re.sub(r"wasn't", "was not", tweet)
        tweet = re.sub(r"don\x89Ûªt", "do not", tweet)
        tweet = re.sub(r"aren't", "are not", tweet)
        tweet = re.sub(r"isn't", "is not", tweet)
        tweet = re.sub(r"What's", "What is", tweet)
        tweet = re.sub(r"haven't", "have not", tweet)
        tweet = re.sub(r"hasn't", "has not", tweet)
        tweet = re.sub(r"There's", "There is", tweet)
        tweet = re.sub(r"He's", "He is", tweet)
        tweet = re.sub(r"It's", "It is", tweet)
        tweet = re.sub(r"You're", "You are", tweet)
        tweet = re.sub(r"I'M", "I am", tweet)
        tweet = re.sub(r"shouldn't", "should not", tweet)
        tweet = re.sub(r"wouldn't", "would not", tweet)
        tweet = re.sub(r"i'm", "I am", tweet)
        tweet = re.sub(r"I\x89Ûªm", "I am", tweet)
        tweet = re.sub(r"I'm", "I am", tweet)
        tweet = re.sub(r"Isn't", "is not", tweet)
        tweet = re.sub(r"Here's", "Here is", tweet)
        tweet = re.sub(r"you've", "you have", tweet)
        tweet = re.sub(r"you\x89Ûªve", "you have", tweet)
        tweet = re.sub(r"we're", "we are", tweet)
        tweet = re.sub(r"what's", "what is", tweet)
        tweet = re.sub(r"couldn't", "could not", tweet)
        tweet = re.sub(r"we've", "we have", tweet)
        tweet = re.sub(r"it\x89Ûªs", "it is", tweet)
        tweet = re.sub(r"doesn\x89Ûªt", "does not", tweet)
        tweet = re.sub(r"It\x89Ûªs", "It is", tweet)
        tweet = re.sub(r"Here\x89Ûªs", "Here is", tweet)
        tweet = re.sub(r"who's", "who is", tweet)
        tweet = re.sub(r"I\x89Ûªve", "I have", tweet)
        tweet = re.sub(r"y'all", "you all", tweet)
        tweet = re.sub(r"can\x89Ûªt", "cannot", tweet)
        tweet = re.sub(r"would've", "would have", tweet)
        tweet = re.sub(r"it'll", "it will", tweet)
        tweet = re.sub(r"we'll", "we will", tweet)
        tweet = re.sub(r"wouldn\x89Ûªt", "would not", tweet)
        tweet = re.sub(r"We've", "We have", tweet)
        tweet = re.sub(r"he'll", "he will", tweet)
        tweet = re.sub(r"Y'all", "You all", tweet)
        tweet = re.sub(r"Weren't", "Were not", tweet)
        tweet = re.sub(r"Didn't", "Did not", tweet)
        tweet = re.sub(r"they'll", "they will", tweet)
        tweet = re.sub(r"they'd", "they would", tweet)
        tweet = re.sub(r"DON'T", "DO NOT", tweet)
        tweet = re.sub(r"That\x89Ûªs", "That is", tweet)
        tweet = re.sub(r"they've", "they have", tweet)
        tweet = re.sub(r"i'd", "I would", tweet)
        tweet = re.sub(r"should've", "should have", tweet)
        tweet = re.sub(r"You\x89Ûªre", "You are", tweet)
        tweet = re.sub(r"where's", "where is", tweet)
        tweet = re.sub(r"Don\x89Ûªt", "Do not", tweet)
        tweet = re.sub(r"we'd", "we would", tweet)
        tweet = re.sub(r"i'll", "I will", tweet)
        tweet = re.sub(r"weren't", "were not", tweet)
        tweet = re.sub(r"They're", "They are", tweet)
        tweet = re.sub(r"Can\x89Ûªt", "Cannot", tweet)
        tweet = re.sub(r"you\x89Ûªll", "you will", tweet)
        tweet = re.sub(r"I\x89Ûªd", "I would", tweet)
        tweet = re.sub(r"let's", "let us", tweet)
        tweet = re.sub(r"it's", "it is", tweet)
        tweet = re.sub(r"can't", "cannot", tweet)
        tweet = re.sub(r"don't", "do not", tweet)
        tweet = re.sub(r"you're", "you are", tweet)
        tweet = re.sub(r"i've", "I have", tweet)
        tweet = re.sub(r"that's", "that is", tweet)
        tweet = re.sub(r"i'll", "I will", tweet)
        tweet = re.sub(r"doesn't", "does not", tweet)
        tweet = re.sub(r"i'd", "I would", tweet)
        tweet = re.sub(r"didn't", "did not", tweet)
        tweet = re.sub(r"ain't", "am not", tweet)
        tweet = re.sub(r"you'll", "you will", tweet)
        tweet = re.sub(r"I've", "I have", tweet)
        tweet = re.sub(r"Don't", "do not", tweet)
        tweet = re.sub(r"I'll", "I will", tweet)
        tweet = re.sub(r"I'd", "I would", tweet)
        tweet = re.sub(r"Let's", "Let us", tweet)
        tweet = re.sub(r"you'd", "You would", tweet)
        tweet = re.sub(r"It's", "It is", tweet)
        tweet = re.sub(r"Ain't", "am not", tweet)
        tweet = re.sub(r"Haven't", "Have not", tweet)
        tweet = re.sub(r"Could've", "Could have", tweet)
        tweet = re.sub(r"youve", "you have", tweet)
        tweet = re.sub(r"donå«t", "do not", tweet)

        # Character entity references
        tweet = re.sub(r"&gt;", ">", tweet)
        tweet = re.sub(r"&lt;", "<", tweet)
        tweet = re.sub(r"&amp;", "&", tweet)

        # Typos, slang and informal abbreviations
        tweet = re.sub(r"w/e", "whatever", tweet)
        tweet = re.sub(r"w/", "with", tweet)
        tweet = re.sub(r"USAgov", "USA government", tweet)
        tweet = re.sub(r"recentlu", "recently", tweet)
        tweet = re.sub(r"Ph0tos", "Photos", tweet)
        tweet = re.sub(r"amirite", "am I right", tweet)
        tweet = re.sub(r"exp0sed", "exposed", tweet)
        tweet = re.sub(r"<3", "love", tweet)
        tweet = re.sub(r"amageddon", "armageddon", tweet)
        tweet = re.sub(r"Trfc", "Traffic", tweet)
        tweet = re.sub(r"8/5/2015", "2015-08-05", tweet)
        tweet = re.sub(r"WindStorm", "Wind Storm", tweet)
        tweet = re.sub(r"8/6/2015", "2015-08-06", tweet)
        tweet = re.sub(r"10:38PM", "10:38 PM", tweet)
        tweet = re.sub(r"10:30pm", "10:30 PM", tweet)
        tweet = re.sub(r"16yr", "16 year", tweet)
        tweet = re.sub(r"lmao", "laughing my ass off", tweet)
        tweet = re.sub(r"TRAUMATISED", "traumatized", tweet)

        # ... and ..
        tweet = tweet.replace('...', ' ... ')
        if '...' not in tweet:
            tweet = tweet.replace('..', ' ... ')

            # Acronyms
        tweet = re.sub(r"MH370", "Malaysia Airlines Flight 370", tweet)
        tweet = re.sub(r"mÌ¼sica", "music", tweet)
        tweet = re.sub(r"okwx", "Oklahoma City Weather", tweet)
        tweet = re.sub(r"arwx", "Arkansas Weather", tweet)
        tweet = re.sub(r"gawx", "Georgia Weather", tweet)
        tweet = re.sub(r"scwx", "South Carolina Weather", tweet)
        tweet = re.sub(r"cawx", "California Weather", tweet)
        tweet = re.sub(r"tnwx", "Tennessee Weather", tweet)
        tweet = re.sub(r"azwx", "Arizona Weather", tweet)
        tweet = re.sub(r"alwx", "Alabama Weather", tweet)
        tweet = re.sub(r"wordpressdotcom", "wordpress", tweet)
        tweet = re.sub(r"usNWSgov", "United States National Weather Service", tweet)
        tweet = re.sub(r"Suruc", "Sanliurfa", tweet)

        # Grouping same words without embeddings
        tweet = re.sub(r"Bestnaijamade", "bestnaijamade", tweet)
        tweet = re.sub(r"SOUDELOR", "Soudelor", tweet)

        return tweet

    @staticmethod
    def fillna(df):
        df.keyword.fillna('no_keyword', inplace=True)
        return df

    @staticmethod
    def duplicate_target(train):

        ids_with_target_error = [328, 443, 513, 2619, 3640, 3900, 4342, 5781, 6552, 6554, 6570, 6701, 6702, 6729, 6861,
                                 7226]
        train['target_relabeled'] = train['target'].copy()
        train.loc[train[
                      'text'] == 'like for the music video I want some real action shit like burning buildings and police chases not some weak ben winston shit', 'target_relabeled'] = 0
        train.loc[train[
                      'text'] == 'Hellfire is surrounded by desires so be careful and donÛªt let your desires control you! #Afterlife', 'target_relabeled'] = 0
        train.loc[train['text'] == 'To fight bioterrorism sir.', 'target_relabeled'] = 0
        train.loc[train[
                      'text'] == '.POTUS #StrategicPatience is a strategy for #Genocide; refugees; IDP Internally displaced people; horror; etc. https://t.co/rqWuoy1fm4', 'target_relabeled'] = 1
        train.loc[train[
                      'text'] == 'CLEARED:incident with injury:I-495  inner loop Exit 31 - MD 97/Georgia Ave Silver Spring', 'target_relabeled'] = 1
        train.loc[train[
                      'text'] == '#foodscare #offers2go #NestleIndia slips into loss after #Magginoodle #ban unsafe and hazardous for #humanconsumption', 'target_relabeled'] = 0
        train.loc[train[
                      'text'] == 'In #islam saving a person is equal in reward to saving all humans! Islam is the opposite of terrorism!', 'target_relabeled'] = 0
        train.loc[train[
                      'text'] == 'Who is bringing the tornadoes and floods. Who is bringing the climate change. God is after America He is plaguing her\n \n#FARRAKHAN #QUOTE', 'target_relabeled'] = 1
        train.loc[train[
                      'text'] == 'RT NotExplained: The only known image of infamous hijacker D.B. Cooper. http://t.co/JlzK2HdeTG', 'target_relabeled'] = 1
        train.loc[train[
                      'text'] == "Mmmmmm I'm burning.... I'm burning buildings I'm building.... Oooooohhhh oooh ooh...", 'target_relabeled'] = 0
        train.loc[
            train['text'] == "wowo--=== 12000 Nigerian refugees repatriated from Cameroon", 'target_relabeled'] = 0
        train.loc[train[
                      'text'] == "He came to a land which was engulfed in tribal war and turned it into a land of peace i.e. Madinah. #ProphetMuhammad #islam", 'target_relabeled'] = 0
        train.loc[train[
                      'text'] == "Hellfire! We donÛªt even want to think about it or mention it so letÛªs not do anything that leads to it #islam!", 'target_relabeled'] = 0
        train.loc[train[
                      'text'] == "The Prophet (peace be upon him) said 'Save yourself from Hellfire even if it is by giving half a date in charity.'", 'target_relabeled'] = 0
        train.loc[train['text'] == "Caution: breathing may be hazardous to your health.", 'target_relabeled'] = 1
        train.loc[train[
                      'text'] == "I Pledge Allegiance To The P.O.P.E. And The Burning Buildings of Epic City. ??????", 'target_relabeled'] = 0
        train.loc[train[
                      'text'] == "#Allah describes piling up #wealth thinking it would last #forever as the description of the people of #Hellfire in Surah Humaza. #Reflect", 'target_relabeled'] = 0
        train.loc[train[
                      'text'] == "that horrible sinking feeling when youÛªve been at home on your phone for a while and you realise its been on 3G this whole time", 'target_relabeled'] = 0
        train.loc[train.id.isin(ids_with_target_error), 'target'] = 0
        train.drop_duplicates(subset='text', keep='first', inplace=True)
        train.reset_index(drop=True, inplace=True)
        return train

    def process_text(self, df):
        if 'target' in df:
            df = self.duplicate_target(df)
        df['cleaned'] = df.text.apply(lambda x: self.clean(x))
        df['cleaned'] = df.cleaned.apply(lambda x: self.remove_emoji(x))
        df['cleaned'] = df.cleaned.apply(lambda x: self.abbra(x))
        df = self.fillna(df)

        return df
