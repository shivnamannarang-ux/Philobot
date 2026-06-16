# Aim to build a chatbot that answers philosophical questions, and indulges in meaningful convos. 
import random
#INTRODUCTION BEGINNING
name = input("Enter your first name:\n").lower().strip() 
if name.startswith("a"): 
    a = ["Awesome", "Ambitious", "Authentic", "Adaptable", "Aesthetic", "Adventurous", "Ace", "Artsy", "Affable", "All-star"]
    print( "Hey",random.choice(a),f"{name.capitalize()}!") 

elif name.startswith("b"):
    b = ["Bold", "Bright", "Brilliant", "Balanced", "Boss", "Bubbly", "Brave", "Big-hearted", "Buzzing", "Badass"]
    print( "Hey",random.choice(b),f"{name.capitalize()}!") 

elif name.startswith("c"):
    c = ["Creative", "Cool", "Confident", "Chill", "Charismatic", "Curious", "Clutch", "Cheerful", "Clever", "Capable"]
    print( "Hey",random.choice(c),f"{name.capitalize()}!") 

elif name.startswith("d"):
    d = ["Driven", "Dynamic", "Dependable", "Daring", "Disciplined", "Down-to-earth", "Determined", "Dazzling", "Dreamy", "Distinctive"]
    print( "Hey",random.choice(d),f"{name.capitalize()}!") 

elif name.startswith("e"):
    e = ["Energetic", "Epic", "Empathetic", "Elite", "Expressive", "Easygoing", "Exciting", "Encouraging", "Eloquent", "Exceptional"]
    print( "Hey",random.choice(e),f"{name.capitalize()}!") 

elif name.startswith("f"):
    f = ["Fearless", "Friendly", "Focused", "Fresh", "Funny", "Fantastic", "Flexible", "Faithful", "Fierce", "Free-spirited"]
    print( "Hey",random.choice(f),f"{name.capitalize()}!") 

elif name.startswith("g"):
    g = ["Genuine", "Grounded", "Gifted", "Generous", "Graceful", "Goal-oriented", "Glowing", "Great-hearted", "Gallant", "Game-changing"] 
    print( f"Hey {random.choice(g)} {name.capitalize()}!")  

elif name.startswith("h"):
    h = ["Honest", "Humble", "Helpful", "Hardworking", "Hilarious", "Hopeful", "Heroic", "Heartwarming", "Hyped", "Harmonious"]
    print( f"Hey {random.choice(h)} {name.capitalize()}!")

elif name.startswith("i"):
    i =  ["Iconic", "Intelligent", "Innovative", "Inspiring", "Insightful", "Independent", "Imaginative", "Influential", "Inventive", "Irreplaceable"]
    print( f"Hey {random.choice(i)} {name.capitalize()}!")

elif name.startswith("j"):
    j = ["Joyful", "Jolly", "Jovial", "Just", "Jazzy", "Judicious", "Jubilant", "Jam-packed", "Jaunty", "Jet-set"]
    print( f"Hey {random.choice(j)} {name.capitalize()}!")

elif name.startswith("k"):
    k = ["Kind", "Keen", "Knowledgeable", "Kingly", "Kickass", "Kindhearted", "Knockout", "Key-player", "Kinetic", "Krisp"]
    print( f"Hey {random.choice(k)} {name.capitalize()}!")

elif name.startswith("l"):
    l = ["Legendary", "Loyal", "Lively", "Lovable", "Level-headed", "Lighthearted", "Limitless", "Lucky", "Leader-like", "Lit"]
    print( f"Hey {random.choice(l)} {name.capitalize()}!")

elif name.startswith("m"):
    m = ["Magnetic", "Mindful", "Motivated", "Mature", "Merciful", "Masterful", "Merry", "Memorable", "Modern", "Majestic"]
    print( f"Hey {random.choice(m)} {name.capitalize()}!")

elif name.startswith("n"):
    n = ["Natural", "Noble", "Nice", "Next-level", "Nimble", "Neat", "Nurturing", "Noteworthy", "Nonstop", "Novel"]
    print( f"Hey {random.choice(n)} {name.capitalize()}!")

elif name.startswith("o"):
    o = ["Optimistic", "Original", "Open-minded", "Outgoing", "Observant", "Outstanding", "Organized", "On-point", "One-of-a-kind", "Overachieving"]
    print( f"Hey {random.choice(o)} {name.capitalize()}!")

elif name.startswith("p"):
    p = ["Positive", "Passionate", "Playful", "Powerful", "Persistent", "Patient", "Practical", "Popular", "Pioneering", "Phenomenal"]
    print( f"Hey {random.choice(p)} {name.capitalize()}!")

elif name.startswith("q"):
    q =  ["Quick-witted", "Quality-driven", "Quirky", "Quietly-confident", "Quick-thinking", "Queenly", "Questing", "Qualified", "Quintessential", "Quick-learning"]
    print( f"Hey {random.choice(q)} {name.capitalize()}!")

elif name.startswith("r"):
    r = ["Radiant", "Reliable", "Resilient", "Respectful", "Resourceful", "Remarkable", "Real", "Refreshing", "Rock-solid", "Revolutionary"]
    print( f"Hey {random.choice(r)} {name.capitalize()}!")

elif name.startswith("s"):
    s = ["Smart", "Sharp", "Strong", "Supportive", "Stylish", "Self-aware", "Steady", "Social", "Spectacular", "Sincere"]
    print( f"Hey {random.choice(s)} {name.capitalize()}!")

elif name.startswith("t"):
    t = ["Thoughtful", "Talented", "Trustworthy", "Tenacious", "Trendy", "Thriving", "Team-player", "Tactical", "Trailblazing", "Top-tier"]
    print( f"Hey {random.choice(t)} {name.capitalize()}!")

elif name.startswith("u"):
    u = ["Unique", "Upbeat", "Unstoppable", "Understanding", "Uplifting", "Ultra-cool", "Unifying", "Unshakeable", "User-friendly", "Ultimate"]
    print( f"Hey {random.choice(u)} {name.capitalize()}!")

elif name.startswith("v"):
    v =  ["Vibrant", "Visionary", "Versatile", "Valiant", "Vibey", "Valuable", "Virtuous", "Vivacious", "Victorious", "Voice-of-reason"]
    print( f"Hey {random.choice(v)} {name.capitalize()}!")

elif name.startswith("w"):
    w = ["Wise", "Witty", "Warm", "Welcoming", "Well-rounded", "Wonderful", "Wholesome", "Winning", "World-class", "Wildly-creative"]
    print( f"Hey {random.choice(w)} {name.capitalize()}!")

elif name.startswith("x"):
    x = ["X-factor", "Xenial", "Xtra-cool", "Xtraordinary", "Xpressive", "Xceptional", "Xciting", "Xpert", "Xuberant", "Xtreme"]
    print( f"Hey {random.choice(x)} {name.capitalize()}!")

elif name.startswith("y"):
    y = ["Youthful", "Yare", "Yielding", "Yummy-vibes", "Yearning", "Yonder-thinking", "Yes-minded", "Yolo-worthy", "Younique", "Yippee-energy"]
    print( f"Hey {random.choice(y)} {name.capitalize()}!")

elif name.startswith("z"):
    z = ["Zesty", "Zen", "Zippy", "Zealous", "Zooming", "Zingy", "Zappy", "Zero-quit", "Zodiac-level", "Zone-dominating"]
    print( f"Hey {random.choice(z)} {name.capitalize()}!")


intro_lines = {
    1: "-Welcome to Philobot, where questions matter more than answers.",
    2: "-Every philosophy began with someone asking 'Why?'.",
    3: "-Enter with curiosity. Leave with better questions.",
    4: "-Philosophy is not about what to think, but how to think.",
    5: "-Greetings, traveler. The world of ideas awaits.",
    6: "-A silent library of thinkers stands before you.",
    7: "-From Socrates to Confucius, many minds await your company.",
    8: "-The unexamined life is not worth living. Let's examine it.",
    9: "-Welcome. Truth may be elusive, but the search is worthwhile.",
    10: "-Choose a path carefully. Every philosophy sees the world differently.",
    11: "-Ideas have shaped civilizations. Today, you explore a few.",
    12: "-Knowledge begins in wonder. Wonder begins here.",
    13: "-The greatest journeys are often intellectual ones.",
    14: "-Every answer creates new questions. That's the fun part.",
    15: "-Step into a conversation that has lasted thousands of years.",
    16: "-Some seek wisdom. Others seek certainty. Philosophy offers neither cheaply.",
    17: "-Behind every philosophy lies a unique way of seeing reality.",
    18: "-The thinkers are ready. The question is: where will you begin?",
    19: "-Welcome to Philobot, a humble guide through the landscape of ideas.",
    20: "-Civilizations rise and fall, but good questions never grow old."
}
print(random.choice(list(intro_lines.values())))
print("-I am a prototype that is learning more about philosophy but can help you get overview of some important school of thoughts all over the world.") 
print("-Which philosophy you would like to start with?")
# INTRODUCTION ENDS 


#MAIN CONTENT BEGINS
while True:
 philosophy = input("Eastern or Western?\n").lower().strip() 
 if philosophy == "eastern": #WHOLE CODE CONSISTS INFO ABOUT EASTERN BRANCH OF PHILOSOPHY 
     #BEGINNING
     print("\n-Your interest seems to be more dramatic and a bit colourful than dried practical philosophies in the west...")
     print("-Well Glad to hear that.") 
     while True:  
      
      origin = input("\n-With which philosophy in the east you would want to start with?\nIndian/Chinese/Islamic\n" ).lower().strip()
      if origin == "indian":
        print('''\nIndian philosophy is one of the oldest and most diverse philosophical traditions in the world.\n-It explores profound questions regarding existence, consciousness, ethics, suffering, liberation, and the nature of reality.\n-Unlike many philosophical traditions that remained largely intellectual, Indian philosophy was deeply connected with practical living, spirituality, meditation, and self-realization.\n-Indian philosophy is broadly divided into two major categories: Āstika and Nāstika schools.\n-Āstika schools accept the authority of the Vedas and include systems such as Vedānta, Sāṃkhya, Yoga, Nyāya, Vaiśeṣika, and Mīmāṃsā.\n-Nāstika schools reject Vedic authority and include Buddhism, Jainism, and Cārvāka philosophy.\n-Major concepts commonly discussed in Indian philosophy include karma (action and consequence), dharma (duty and moral order), moksha (liberation), rebirth, self-discipline, and the search for ultimate truth.\n-Different schools offer different paths toward understanding reality and attaining liberation.\n-Indian philosophy influenced not only religion and spirituality in India but also psychology, ethics, meditation practices, literature, and modern philosophical discussions across the world.''')
        while True:
         indian = input("\n-Which aspect you are more interested in Aastika/Nastika?\n").lower().strip()
         if indian == "aastika": 
            print('''\n-Āstika schools of Indian philosophy are the traditions that accept the authority of the Vedas, the ancient sacred texts of India.\n-But do not mistake them for blind belief systems.\n-These schools were deeply intellectual and asked difficult questions about reality, consciousness, suffering, logic, ethics, and liberation.\n-The fascinating part is that Āstika philosophy is not a single idea. It contains multiple schools like Vedānta, Yoga, Nyāya, Sāṃkhya, and Mīmāṃsā, each offering a different interpretation of existence and truth.\n-Some focused on meditation and inner realization, some on logic and reasoning, while others explored the nature of the soul and universe itself.\n-Rather than asking merely “What should we believe?”, Āstika philosophies often asked:“Who are we beneath our thoughts, desires, and identities?”\n-And that question alone shaped centuries of spiritual and philosophical exploration in India.''')
            break
         elif indian == "nastika": 
            print('''\n-Nāstika schools of Indian philosophy are the traditions that rejected the authority of the Vedas and challenged many accepted religious assumptions of their time.\n-But this rejection was not mere rebellion. It was an intense intellectual movement driven by questioning, observation, logic, and independent inquiry.\n-Schools such as Buddhism, Jainism, and Cārvāka emerged from this tradition, each offering radically different views about reality, morality, suffering, and liberation. \n-Some denied the existence of a permanent soul, some rejected ritualism, while others focused entirely on direct experience rather than sacred authority.
-What makes Nāstika philosophies fascinating is their courage to ask uncomfortable questions:

“Must truth depend on tradition?”
“Can suffering be understood without relying on divine explanations?”
“Is human experience itself enough to understand reality?”

-These schools transformed Indian philosophy into a battlefield of ideas, where even the oldest beliefs could be questioned, debated, and reimagined.''')
            break
         else:
            print("\n-Please enter the name out of the options given below:")  
        break
        
      elif origin == "chinese":
        print('''\n-Chinese philosophy is one of the most refined and practical philosophical traditions in human history.\n-Rather than obsessing only over abstract theories, it focused deeply on harmony, balance, ethics, leadership, self-discipline, and the art of living wisely within society and nature.\n-Major schools such as Confucianism, Daoism (Taoism), and Chinese Buddhism approached life in very different ways.\n-Confucianism emphasized morality, responsibility, and social order.\n-Daoism encouraged people to flow naturally with existence rather than forcing control over everything.\n-Chinese Buddhism explored suffering, consciousness, compassion, and inner awakening.

-What makes Chinese philosophy truly fascinating is its calm realism. Instead of asking only:
“What is the ultimate truth?”
it often asked:
“How should a human being live in a chaotic world?”

-Its ideas influenced politics, martial arts, medicine, spirituality, governance, and everyday life across East Asia for centuries, shaping entire civilizations through wisdom rather than conquest alone.''')
        while True:  
         chinese = input("\n-Choose the chinese philosophy you would like to study - Confucianism, Daoism (Taoism) or Chinese Buddhism \n").lower().strip()
         if chinese == "confucianism":
           print('''\n-Confucianism is a Chinese philosophical tradition founded upon the teachings of Confucius, a thinker who believed that the strength of a civilization depends not merely on laws or power, but on the moral character of its people.\n-Rather than focusing heavily on gods or the afterlife, Confucianism concentrated on ethics, discipline, respect, responsibility, and social harmony.\n-It taught that a stable society begins with self-cultivation. A person who learns respect, honesty, wisdom, and compassion naturally improves their family, community, and eventually the state itself. In this way, personal morality and political order were deeply connected.

-What makes Confucianism fascinating is its practical and deeply human approach. It asks:

“What kind of person should one become?”
“How should humans treat one another?”
“Can society function without virtue?”

-For centuries, Confucianism shaped Chinese education, governance, culture, and family structures, turning philosophy into a guide for everyday conduct rather than mere abstract speculation.''')
           break
          
         elif chinese == "daoism" or chinese == "taoism":
           print('''\n-Daoism, also known as Taoism, is a Chinese philosophical tradition that teaches harmony with the natural flow of existence, known as the Dao or “The Way.”\n-Instead of forcing control over life, Daoism encourages balance, simplicity, spontaneity, and alignment with nature.\n-Founded upon the teachings associated with Laozi and texts such as the "Dao De Jing", Daoism viewed excessive ambition, rigid rules, and constant struggle as sources of human suffering.\n-It suggested that many problems arise because people try too hard to dominate life rather than understand its rhythm.\n-One of its most fascinating ideas is "Wu Wei", often translated as “effortless action” or “action without force.”\n-It does not mean laziness, but acting in harmony with situations instead of against them, much like water flowing naturally around obstacles while still shaping mountains over time.

-Daoism asks subtle but powerful questions:

“Must strength always be aggressive?”
“Can softness overcome rigidity?”
“What happens when humans stop fighting the natural order of existence?”

-Its influence can be seen in Chinese spirituality, martial arts, medicine, poetry, meditation, and even strategies of leadership and warfare.''')
           break
          
         elif chinese == "chinese buddhism": 
           print('''\n-Chinese Buddhism emerged when the teachings of Buddhism from India entered China and gradually blended with Chinese culture, Daoist thought, and local traditions.\n-Over time, it evolved into a unique philosophical and spiritual system focused on suffering, consciousness, compassion, mindfulness, and inner awakening.\n-Unlike purely ritualistic religion, Chinese Buddhism deeply explored the nature of the human mind.\n-It taught that suffering often arises from attachment, ignorance, and uncontrolled desires, and that true peace comes through wisdom, self-awareness, and compassion toward all living beings.\n-What makes Chinese Buddhism especially fascinating is the way it merged deep spirituality with simplicity and everyday life. Schools such as Chan Buddhism, which later became Zen in Japan, emphasized direct experience over endless intellectual debate.\n-Instead of merely asking people to believe, it encouraged them to observe their own minds directly.

-Chinese Buddhism asks profound questions:

“Why does the mind suffer even when desires are fulfilled?”
“Can silence reveal truths that words cannot?”
“What remains when the ego becomes still?”

-Its influence shaped Chinese art, meditation, poetry, philosophy, martial arts, and spiritual traditions for centuries, leaving behind a legacy centered not on domination, but on inner transformation.''')
           break
          
         else: 
           print("\n-Please enter the name out of the options given below:")
        
        
        break
     
      elif origin == "islamic": 
        print('''\n-Islamic philosophy is a rich intellectual tradition that emerged through the interaction of Islamic teachings with logic, metaphysics, science, ethics, and ancient Greek philosophy. Rather than being limited only to theology, it became a vast exploration of existence, knowledge, reason, consciousness, morality, and the relationship between humanity and the Divine.\n-Thinkers such as Al-Farabi, Ibn Sina (Avicenna), Al-Ghazali, and Ibn Rushd (Averroes) debated profound questions regarding free will, the soul, reality, faith, and rationality. Different schools like Kalam, Falsafa, and Sufism approached these questions in distinct ways.\n-Some emphasized logic and philosophical reasoning, while others focused on spiritual experience and inner purification.

-What makes Islamic philosophy fascinating is its attempt to reconcile revelation with reason. It asked:

“Can human intellect understand ultimate truth?”
“What is the nature of the soul?”
“Is reason enough, or does wisdom require spiritual awakening as well?”

-Islamic philosophy greatly influenced science, mathematics, medicine, ethics, spirituality, and even European intellectual traditions during the medieval period, becoming one of the most important centers of philosophical inquiry in world history.''') 
        while True: 
          islamic = input("\n-There are major three schools of thoughts in Islamic Philosophy: Kalam/Falsafa/Sufism.\n-Choose one of them.\n").lower().strip() 
          if islamic == "kalam":
            print('''\n-Kalam is a major school of Islamic philosophy and theology that focused on using logic and rational debate to understand and defend religious beliefs.\n-Rather than accepting ideas blindly, scholars of Kalam engaged in deep intellectual discussions about existence, free will, morality, the nature of God, the soul, and the origins of the universe.\n-What makes Kalam fascinating is that it transformed faith into a field of rigorous philosophical inquiry.

-Thinkers debated questions such as:

“Does humans truly possess free will?”
“Can reason alone prove the existence of God?”
“Is the universe eternal, or did it have a beginning?”

-Different schools within Kalam developed different approaches, but all shared a commitment to critical reasoning and structured argumentation. In many ways, Kalam became one of the earliest sophisticated traditions of philosophical theology, where belief and logic were brought into direct conversation rather than treated as opposites.Its influence extended beyond religion into ethics, metaphysics, science, and intellectual culture across the Islamic world for centuries.''')
            break
           
          elif islamic == "falsafa": 
            print('''\n-Falsafa was the philosophical tradition within the Islamic world that sought to understand reality through reason, logic, and intellectual inquiry, drawing heavily from Greek philosophers such as Aristotle and Plato.\n-Unlike purely theological approaches, Falsafa emphasized rational thinking, metaphysics, ethics, science, and the systematic exploration of existence.\n-Philosophers such as Al-Farabi, Ibn Sina (Avicenna), and Ibn Rushd (Averroes) became central figures of this tradition.\n-They explored profound questions regarding the soul, consciousness, causality, knowledge, and the relationship between reason and revelation.\n-Many of them believed that human intellect was capable of uncovering deep truths about the universe and existence.

-What makes Falsafa fascinating is its bold confidence in rational inquiry. It asked:

“Can philosophy and faith coexist?”
“Can logic lead humans toward ultimate truth?”
“What is the true nature of existence and consciousness?”

-Falsafa became one of the most intellectually sophisticated traditions of the medieval world, influencing not only Islamic civilization but also European philosophy, science, medicine, and logic for centuries afterward.''')
            break
          
          elif islamic == "sufism": 
            print('''\n-Sufism is the mystical dimension of Islamic philosophy and spirituality that focuses on inner transformation, self-purification, love, and direct spiritual experience of the Divine.\n-Rather than concentrating only on external rituals or intellectual debate, Sufism seeks to understand truth through the purification of the heart and deep spiritual awareness.\n-Sufi thinkers and poets such as Rumi, Al-Ghazali, Ibn Arabi, and Rabia al-Basri explored profound themes of love, ego, suffering, devotion, and the human longing for transcendence.\n-They believed that beneath worldly distractions and the restless ego lies a deeper reality that can only be experienced through sincerity, remembrance, discipline, and inner awakening.

-What makes Sufism especially fascinating is its deeply poetic and emotional approach toward spirituality. It asks:

“Who are we beneath the ego?”
“Can love become a path toward truth?”
“What happens when the self becomes silent?”

-Sufism influenced poetry, music, art, meditation, ethics, and spiritual traditions across the Islamic world for centuries, turning philosophy not merely into intellectual discussion, but into a journey of inner transformation.''')
            break
          
          else: 
            print ("\n-Please enter the name out of the options given below:")
        break
            
            
      else: 
        print("\n-Please enter the name out of the options given below:")

     input("\n-Press Enter to exit:\n") 
     break

 #END 
 
 
 
 
 
 
 
 
 elif philosophy == "western": #WHOLE BRANCH CONSISTS INFO ABOUT WESTERN BRANCH OF PHILOSOPHY
  #BEGINNING
  print("\n-Mhm.... you seem more inclined towards blunt and practical philosophy of the west... rather than the exaggerated fairy tale versions of the east.") 
  print("\n-The experience is gonna be amazing.") 
  while True: 
    western = input("\n-Western philosophies differ with respect to time period, it includes - Ancient/Modern/Contemporary philosophies.\n-Enter the name of philosophy you want to continue with.\n-").lower().strip()
    if western == "ancient": 
      print('''\n-Ancient Western philosophy began in ancient Greece, where thinkers first started questioning the nature of reality, knowledge, morality, politics, and human existence through reason rather than mythology alone.\n-Instead of simply accepting traditional beliefs, philosophers began asking bold and unsettling questions about truth, justice, happiness, and the structure of the universe itself.\n-Thinkers such as Socrates, Plato, Aristotle, Diogenes, Epicurus, and Zeno founded influential schools of thought that shaped not only philosophy, but also science, politics, logic, ethics, and education for centuries afterward.\n-Some focused on logic and knowledge, others on self-control, virtue, pleasure, or freedom from suffering.

-What makes Ancient philosophy fascinating is its fearless curiosity. These philosophers questioned everything:

“What makes a life meaningful?”
“Can truth be discovered through reason?”
“Should humans follow society, pleasure, virtue, or nature?”
“What does it truly mean to live wisely?”

-Ancient philosophy became the intellectual foundation of much of Western civilization, influencing law, governance, psychology, ethics, and even modern debates about meaning and human nature thousands of years later.''')
      while True:
        ancient = input("\n-The ancient philosophy's river is mainly contributed by three philosophical tributaries - Stoicism/Epicureanism/Cynicism.\n-Enter the name of the tributary would you like to have a look into.\n-").lower().strip()
        if ancient == "stoicism": 
          print('''\n-Stoicism is an ancient Greek philosophy founded upon the idea that true strength comes not from controlling the world, but from controlling one’s reactions to it.\n-Developed by thinkers such as Zeno, Seneca, Epictetus, and Marcus Aurelius, Stoicism taught that suffering often arises because humans become emotionally enslaved to things beyond their control.\n-Rather than chasing constant pleasure, wealth, or social approval, Stoics focused on discipline, wisdom, resilience, and inner peace.\n-They believed that external events are unpredictable, but the human mind can still remain calm, rational, and dignified amidst chaos.

-What makes Stoicism especially powerful is its brutally practical nature. It asks:

“What truly lies within our control?”
“Can adversity become a source of strength?”
“Why allow temporary events to dominate the mind?”

-Stoicism does not teach emotional suppression, but emotional mastery. Its teachings continue to influence psychology, leadership, self-improvement, and modern discussions about mental resilience, proving that a philosophy created thousands of years ago still speaks directly to the anxieties of modern life.''')
          break

        elif ancient == "epicureanism": 
          print('''\n-Epicureanism is an ancient Greek philosophy founded by Epicurus, centered around the pursuit of peace, happiness, and freedom from unnecessary suffering.\n-Contrary to popular misunderstanding, Epicureanism was not about reckless pleasure or endless luxury. Instead, it taught that true happiness comes from simplicity, wisdom, friendship, and a calm mind free from fear and anxiety.\n-Epicurus believed that many human beings suffer because they endlessly chase wealth, power, status, and temporary desires, only to remain dissatisfied.\n-He argued that a peaceful life is achieved not through excess, but through moderation, self-understanding, and the removal of unnecessary mental turmoil.

-What makes Epicureanism fascinating is its deeply psychological insight. It asks:

“Do humans suffer more from reality, or from their endless desires?”
“Can simplicity create deeper happiness than luxury?”
“What if peace of mind is greater than pleasure itself?”

-Epicureanism encouraged people to value meaningful friendships, thoughtful living, and inner tranquility over social obsession and material ambition, making it one of the earliest philosophies focused on mental well-being and sustainable happiness.''')
          break
        
        elif ancient == "cynicism": 
          print('''\n-Cynicism is an ancient Greek philosophy that rejected society’s obsession with wealth, status, luxury, and social approval.\n-Founded by thinkers such as Antisthenes and most famously Diogenes, Cynicism argued that many human problems arise because people become enslaved to artificial desires and societal expectations rather than living naturally and honestly.\n-Cynics believed that virtue, self-sufficiency, and freedom from material dependence were far more valuable than power or reputation.\n-They openly criticized hypocrisy, greed, vanity, and the shallow behavior of society, often through sharp humor, shocking actions, and fearless honesty.

-What makes Cynicism fascinating is its rebellious and brutally direct nature. It asks:

“Are humans genuinely free, or controlled by social expectations?”
“Why chase status that disappears with time?”
“What remains of a person when luxury, fame, and approval are stripped away?”

-Diogenes, the most famous Cynic, became legendary for mocking social conventions and exposing human pretensions with biting simplicity. Cynicism challenged people not merely to think differently, but to live differently, turning philosophy into an act of resistance against artificial living.''')
          break
        
        else: 
          print("\n-Please choose one of the options given below:")
  
      break

    if western == "modern": 
      print('''\n-Modern Western philosophy emerged during a time when Europe was undergoing massive transformations in science, politics, religion, and human thought.\n-Philosophers began shifting away from unquestioned tradition and authority, instead emphasizing reason, observation, individual freedom, skepticism, and human understanding.\n-Thinkers such as René Descartes, John Locke, David Hume, Immanuel Kant, Nietzsche, and Jean-Paul Sartre explored profound questions regarding knowledge, reality, morality, freedom, identity, and the meaning of existence.\n-Some believed reason was the ultimate path to truth, while others argued that experience, perception, or even personal struggle shaped human understanding.
            
-What makes Modern philosophy fascinating is its intense intellectual rebellion. It challenged ancient assumptions and asked:

“How can humans know what is truly real?”
“Is morality universal or created by society?”
“Are humans genuinely free?”
“What gives life meaning in a world filled with uncertainty?”

-Modern philosophy deeply influenced science, democracy, psychology, politics, education, and modern culture itself, transforming philosophy from ancient speculation into a direct confrontation with the modern human condition.''')
      while True: 
        modern = input ("\n-Modern Philosophy is made up of three prominent philosophy - Rationalism/Empiricism/Existentialism.\n-Enter the Name of the philosophy you would like to continue with.\n-").lower().strip()
        if modern == "rationalism": 
          print('''\n-Rationalism is a major branch of modern Western philosophy that argues that reason and logical thinking are the primary sources of true knowledge.\n-Rationalist philosophers believed that human intellect possesses the ability to discover deep truths about reality, existence, mathematics, morality, and even the universe itself without relying entirely on sensory experience.\n-Thinkers such as René Descartes, Baruch Spinoza, and Gottfried Leibniz became central figures of this tradition. They questioned whether human senses could always be trusted, since perception can often be deceptive or limited. Instead, they argued that certain truths can be reached through pure reasoning and intellectual analysis.

-What makes Rationalism fascinating is its radical confidence in the power of the human mind. It asks:

“Can reason uncover truths beyond physical experience?”
“If the senses can deceive us, what can humans truly trust?”
“Are some ideas already present within the mind itself?”

-One of the most famous Rationalist ideas came from Descartes, who declared:
“I think, therefore I am.”
By doubting everything except the existence of his own thinking mind, he attempted to build knowledge upon absolute certainty.

-Rationalism greatly influenced science, mathematics, logic, and modern philosophy, shaping the belief that disciplined reasoning could help humanity understand both reality and itself.''')
          break

        if modern == "empiricism": 
          print('''\n-Empiricism is a major branch of modern Western philosophy that argues that knowledge primarily comes from experience and observation rather than pure reasoning alone.\n-Empiricist philosophers believed that the human mind begins as a “blank slate,” and that understanding is gradually built through sensory experience, experimentation, and interaction with the world.\n-Thinkers such as John Locke, George Berkeley, and David Hume became central figures of this tradition.\n-They questioned the idea that humans are born with innate knowledge and instead emphasized seeing, hearing, touching, observing, and experiencing reality directly.

-What makes Empiricism fascinating is its grounding in observable reality. It asks:

“How can humans claim knowledge without evidence?”
“If experience shapes understanding, then how reliable are our perceptions?”
“Can truth exist independently of observation?”

-Empiricism became one of the philosophical foundations of modern science because it encouraged experimentation, evidence, and skepticism instead of blind assumption. Its influence transformed not only philosophy, but also psychology, scientific inquiry, education, and the modern understanding of how humans learn about the world.''')
          break

        if modern == "existentialism": 
          print('''\n-Existentialism is a modern Western philosophy that focuses on human freedom, individuality, choice, and the search for meaning in an uncertain world. Rather than providing fixed answers about life, Existentialism confronts the anxiety, confusion, isolation, and responsibility that come with being human.\n-Thinkers such as Søren Kierkegaard, Friedrich Nietzsche, Jean-Paul Sartre, Albert Camus, and Simone de Beauvoir explored questions surrounding existence, purpose, morality, authenticity, and personal identity.\n-They believed that humans are not born with predefined meaning. Instead, individuals must create meaning through their choices, actions, and way of living.

-What makes Existentialism fascinating is its deeply personal and unsettling nature. It asks:

“If life has no predetermined purpose, what should humans live for?”
“Are humans truly free, even when freedom feels terrifying?”
“Can meaning still exist in a world filled with suffering and uncertainty?”

-Existentialism emphasizes personal responsibility and authenticity. It challenges people to confront reality honestly rather than hide behind social expectations, blind conformity, or comforting illusions. Its ideas influenced psychology, literature, art, politics, and modern discussions about identity, alienation, and the struggle to find meaning in contemporary life.In many ways, Existentialism is less about providing comfort and more about forcing humans to confront themselves directly. Which explains why so many existentialist writers sounded simultaneously brilliant and exhausted.''')
          break
        else: 
          print("\n-Please choose one of the options given below:")

      break

    if western == "contemporary":
      print('''\n-Contemporary philosophy refers to the diverse philosophical movements and ideas that developed mainly during the 20th and 21st centuries, as thinkers began confronting the complexities of modern life, technology, politics, language, identity, media, science, and rapidly changing social structures.\n-Unlike older philosophies that often searched for universal truths, contemporary philosophy frequently questions whether absolute truth, certainty, or objective meaning can even exist.\n-Thinkers such as Michel Foucault, Jacques Derrida, Ludwig Wittgenstein, Bertrand Russell, Karl Marx, Simone de Beauvoir, and Martin Heidegger explored issues related to language, power, consciousness, society, freedom, identity, gender, technology, and human perception.\n-Different schools emerged, including Analytic Philosophy, Phenomenology, Postmodernism, Structuralism, and Marxism, each examining reality from very different perspectives.
-What makes Contemporary philosophy fascinating is its willingness to question not only society, but also the systems through which humans understand reality itself. It asks:

“Do humans see reality directly, or through social and linguistic filters?”
“How do power structures shape truth and morality?”
“Can identity remain stable in a constantly changing world?”
“What happens to meaning in an age dominated by technology and information?”

-Contemporary philosophy deeply influences modern psychology, politics, media studies, literature, sociology, gender studies, and cultural criticism. Rather than offering simple answers, it often forces people to confront uncomfortable ambiguities about modern existence itself.Which is fitting, because modern life increasingly resembles a civilization trying to philosophize while simultaneously scrolling endlessly through notifications.''') 
      while True: 
        contemporary = input("\n-Contemporary philosophy has mainly three branches - Nihilism/Postmodernism/Marxism, enter the name of the branch you would like to study.\n-").lower().strip()
        if contemporary == "nihilism": 
          print('''\n-Nihilism is a philosophical perspective that questions or rejects the existence of inherent meaning, objective morality, absolute truth, or predetermined purpose in life.\n-It emerged most powerfully in modern Western thought through thinkers such as Friedrich Nietzsche, who examined what happens when traditional beliefs, values, and certainties begin to collapse.\n-At its core, Nihilism confronts a deeply unsettling possibility:

“What if the universe itself has no built-in meaning?”

-For many, this idea appears dark or pessimistic. But Nihilism is more complex than simple hopelessness.\n-Some forms of Nihilism merely argue that humans create meaning rather than discovering it already embedded within reality. Others challenge social norms, moral systems, or assumptions about truth itself.
-What makes Nihilism fascinating is its brutal honesty and psychological intensity. It asks:

“If there is no ultimate meaning, how should humans live?”
“Are morality and purpose universal truths, or human inventions?”
“Can freedom become overwhelming when nothing is inherently certain?”

-Nietzsche feared that societies losing old beliefs without creating new values could fall into despair and emptiness. Yet he also believed this collapse could become an opportunity for humans to create their own meaning, values, and direction.

-Nihilism continues to influence literature, psychology, philosophy, films, and modern culture because it directly confronts one of humanity’s oldest fears:
“What if existence itself is indifferent to us?” ''') 
          break
 
        if contemporary == "postmodernism": 
          print('''\n-Postmodernism is a contemporary philosophical movement that questions the existence of absolute truths, fixed meanings, and universal explanations of reality.\n-Emerging strongly during the 20th century, Postmodernism challenged the confidence of earlier philosophies that believed reason, science, religion, or political systems could fully explain human existence.\n-Thinkers such as Michel Foucault, Jacques Derrida, Jean-François Lyotard, and Jean Baudrillard explored how language, culture, media, power, and social systems shape the way humans perceive truth and reality.\n-According to many postmodern thinkers, what people often call “truth” may actually be influenced by history, politics, institutions, and cultural narratives rather than being completely objective.

-What makes Postmodernism fascinating is its deep skepticism toward certainty itself. It asks:

“Can humans ever see reality without cultural filters?”
“Who decides what is considered truth or normal?”
“Are identities fixed, or constantly constructed by society and language?”

-Postmodernism also examined how media, consumer culture, and modern institutions influence human thought and behavior. It became highly influential in literature, art, sociology, politics, media studies, and cultural criticism.Critics argue that Postmodernism can become too skeptical or confusing, while supporters believe it exposes hidden assumptions and power structures within society. In many ways, Postmodernism reflects the fragmented and information-saturated nature of modern life itself, where certainty becomes increasingly difficult to hold onto.''')
          break

        if contemporary == "marxism":
          print('''\n-Marxism is a political, economic, and philosophical tradition developed primarily from the ideas of Karl Marx and Friedrich Engels.\n-It examines how societies are shaped by class struggle, economic systems, labor, and the distribution of power and wealth. Rather than viewing history merely as a sequence of kings, wars, or great individuals, Marxism argues that material conditions and economic structures deeply influence human society and behavior.\n-According to Marxism, societies throughout history have often been divided between those who control wealth and production and those who provide labor.\n-In capitalist systems, Marx argued that workers can become alienated from their labor, exploited for profit, and trapped within systems that prioritize wealth accumulation over human well-being.

-What makes Marxism fascinating is its intense focus on power, inequality, and social structures. It asks:
                
“Who truly benefits from economic systems?”
“Can freedom exist alongside severe inequality?”
“How do wealth and power shape morality, politics, and culture?”

-Marxism was not merely a theory about economics. It became a major force influencing revolutions, political movements, sociology, labor rights, economics, and critiques of capitalism across the world. Some view it as a powerful analysis of inequality and exploitation, while others criticize the authoritarian systems that emerged under certain Marxist governments. Whether admired or criticized, Marxism remains one of the most influential and debated philosophies in modern history because it directly confronts the relationship between power, labor, and human society itself.''')
          break

      break 

  input("\n-Press Enter to exit:\n")
  break 
 
 
 else: 
  print ("-Please enter the name out of the options given below:") 
#END      
     