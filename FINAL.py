#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


questions = [
"How's the mental chatter been treating you lately? Any shifts in the soundtrack?",

"Getting cozy under the covers lately? Any insights into your sleep adventures?",

"Any unexpected cravings knocking on your door recently?",

"Feeling the spark for your favorite pastimes or is it a bit dimmer these days?",

"Are there shadows in your thoughts, or is the sunshine winning?",

"Feeling like a fully charged battery or running on low power?",

"Any surprises on the scale lately? Weighty matters or just minor fluctuations?",

"Confidence levels: soaring high or taking a bit of a breather?",

"Any guilt trips taking you on an unexpected journey?",

"Temperature check: cool breeze or a bit of a heatwave?",

"Any unexpected guests in the attic of your mind?",

"Are decisions flowing smoothly or encountering a few detours?",

"Social butterfly or cozying up with a good book?",

"Motivation meter: revved up or idling?",

"Gym enthusiast or Netflix connoisseur?",

"Stress magnet or stress repellent?",

"Any unexpected twinges or aches throwing you off your game?",

"Joyometer: hitting the high notes or a bit off-key?",

"Focus lens: crystal clear or slightly foggy?",

"Restless nights or sleeping like a baby?",

"Culinary adventures or sticking to the classics?",

"Inner critic: whispering encouragement or casting shadows?",

"Social scene: buzzing with activity or enjoying some quiet time?",

"Feeling like a rockstar or questioning your shine?",

"Dreamy nights or wrestling with the sandman?",

"Navigating responsibilities like a pro or feeling a bit adrift?",

"Dusting off hobbies or catching up on Netflix?",

"Feeling like you're in the fast lane or stuck in traffic?",

"Weathering the storm or basking in sunshine?",

"Decision-making: snap judgments or pondering each move?",

"Embracing intimacy or needing some space?",

"Initiating tasks: diving in headfirst or dipping your toes?",

"Confidence levels: sky-high or needing a boost?",

"Emotional landscape: a kaleidoscope of colors or shades of gray?",

"Patience: flowing freely or running a bit thin?",

"Joy levels: fireworks or sparklers?",

"Grooming game: on fleek or could use a touch-up?",

"Attention span: marathon runner or sprinter?",

"Self-worth: solid as a rock or a bit wobbly?",

"Handling criticism: like water off a duck's back or feeling the sting?",

"Social scene: life of the party or preferring one-on-one time?",

"Weight fluctuations: smooth sailing or a bit choppy?",

"Anxiety levels: calm waters or a bit choppy?",

"Passion for work/study: burning brightly or in need of a spark?",

"Decision compass: pointing true north or spinning?",

"Task initiation: ready, set, go or hesitating at the starting line?",

"Finding joy in the everyday or searching for hidden treasures?",

"Self-motivated or needing a push?",

"Conversationalist extraordinaire or lost in thought?",

"Daydreamer or firmly grounded?",

"Alone time: refreshing or feeling a bit too quiet?",

"Content with productivity or craving more?",

"Seeking joy in the small moments or feeling stuck in a rut?",

"Any lingering frustrations bubbling under the surface?",

"Navigating setbacks: smooth sailing or hitting rough waters?",

"Social engagement: party planner or more of a homebody?",

"Feeling the weight of responsibility or embracing it?",

"Adapting to change: surfing the waves or feeling a bit seasick?",

"Stress relief rituals: a daily necessity or often forgotten?"
]
prompts = [
"How's your sleep been lately? Rating it on a scale of 'dreamy' to 'tossing and turning'?",

"What's the typical bedtime routine for a guy like you?",

"Feeling more like a daytime dynamo or a nighttime ninja when it comes to energy?",

"What's on the menu for keeping you fueled and ready for action?",

"Any Jedi mind tricks for keeping stress at bay?",

"Got any hygiene hacks that keep you feeling fresh?",

"What keeps your mental gears grinding throughout the day?",

"How do you make sure your meals are hitting all the right spots?",

"Ever notice how chowing down affects your mood and mojo?",

"What's your secret sauce for keeping that physical engine revving?",

"How's your mood been lately? Are you riding high on positivity or feeling a bit cloudy?",

"Describe your go-to relaxation ritual. Is it more 'zen master' or 'unwinding chaos'?",

"When it comes to tackling challenges, are you more of a 'calm and collected' type or a 'fly by the seat of your pants'?",

"What's your trick for staying motivated? Are you more about setting big goals or taking it one step at a time?",

"Any tips for maintaining focus during a busy day? Are you more about deep concentration or juggling multiple tasks?",

"Tell me about your downtime. Are you all about Netflix binges or outdoor adventures?",

"How do you recharge your batteries after a long day? Are you more into solo relaxation or socializing?",

"When it comes to managing responsibilities, are you a meticulous planner or a spontaneous problem solver?",

"What's your approach to self-care? Do you prefer indulging in pampering sessions or keeping it simple?",

"How do you handle setbacks? Are you more about bouncing back quickly or taking time to regroup?",
]


# In[3]:


options = [
    ['a. Chill as usual', 'b. Kinda scatterbrained', 'c. Lost in thought a lot', 'd. Totally spaced out'],
    ['a. Sleeping like a baby', 'b. Bit all over the place', 'c. Insomnia\'s a new friend', 'd. Bed\'s my new BFF or avoiding it at all costs'],
    ['a. Eating like a champ', 'b. Snacking a bit more or less', 'c. Rollercoaster of hunger', 'd. Food\'s like a stranger to me'],
    ['a. Still my jam', 'b. Meh, kinda into it', 'c. Rarely feeling it', 'd. What\'s excitement?'],
    ['a. Nope, all good', 'b. Sometimes feeling it', 'c. Frequently hopeless', 'd. Living in a hope desert'],
    ['a. Energizer bunny', 'b. Up and down', 'c. Mostly on low', 'd. Out of battery'],
    ['a. Rocking the usual', 'b. A bit up or down', 'c. Major shift on the scale', 'd. Rollercoaster ride'],
    ['a. Confidence for days', 'b. Average vibes', 'c. Kinda shaky', 'd. Confidence who?'],
    ['a. Guilt-free zone', 'b. Occasionally guilty', 'c. Frequently guilty', 'd. Guilt\'s my shadow'],
    ['a. Zen master', 'b. Slightly irritable', 'c. Easily annoyed', 'd. Human volcano'],
    ['a. Sunshine and rainbows', 'b. Rarely', 'c. Sometimes', 'd. Dark clouds only'],
    ['a. Decision-making guru', 'b. Decent, I guess', 'c. Hard to decide', 'd. Decision-making is a myth'],
    ['a. Socializing pro', 'b. Here and there', 'c. Avoiding crowds', 'd. Socializing? What\'s that?'],
    ['a. Killing it', 'b. Getting stuff done', 'c. Struggling', 'd. Tasks? Not today'],
    ['a. Fitness fanatic', 'b. Some exercise', 'c. Minimal effort', 'd. Exercise? Never heard of it'],
    ['a. Handling stress like a boss', 'b. Managing okay', 'c. Stress levels rising', 'd. Stress is my roommate'],
    ['a. Feeling great', 'b. A bit uncomfortable', 'c. Quite painful', 'd. Pain\'s my new friend'],
    ['a. Happy vibes only', 'b. Some joy here and there', 'c. Rarely joyful', 'd. Joy? What\'s that?'],
    ['a. Super focused', 'b. Okay-ish', 'c. Hard to concentrate', 'd. Concentration who?'],
    ['a. Chillaxed', 'b. A bit restless', 'c. Often restless', 'd. Restless soul'],
    ['a. Eating like a champ', 'b. A bit off', 'c. Not feeling hungry or always hungry', 'd. Food\'s a stranger'],
    ['a. Positive vibes only', 'b. Some negativity', 'c. Frequently negative', 'd. Negativity on repeat'],
    ['a. Socializing pro', 'b. Here and there', 'c. Social interactions are draining', 'd. Socializing? Nah.'],
    ['a. Confident and worthy', 'b. Doubting a bit', 'c. Frequently doubting', 'd. Worthless vibes'],
    ['a. Sleeping like a baby', 'b. A bit restless', 'c. Sleep\'s a challenge', 'd. Dreamless nights'],
    ['a. Responsible as always', 'b. Managing okay', 'c. Struggling', 'd. Responsibility who?'],
    ['a. Hobbies thriving', 'b. Some interest left', 'c. Lost interest', 'd. Hobbies? What are those?'],
    ['a. Full of energy', 'b. Sometimes sluggish', 'c. Frequently sluggish', 'd. Energy levels depleted'],
    ['a. Easy breezy', 'b. Handling it', 'c. Feeling overwhelmed', 'd. Life\'s a storm'],
    ['a. Decisions are a breeze', 'b. Decent decisions', 'c. Hard to decide', 'd. Decisions? No thanks.'],
    ['a. Intimacy champion', 'b. Okay-ish', 'c. Feeling disconnected', 'd. Intimacy? What\'s that?'],
    ['a. Task master', 'b. Some tasks get done', 'c. Struggling to complete tasks', 'd. Tasks? Never started.'],
    ['a. Confidence for days', 'b. Average vibes', 'c. Kinda shaky', 'd. Confidence who?'],
    ['a. Emotionally expressive', 'b. Sometimes numb', 'c. Frequently numb', 'd. Emotions on mute'],
    ['a. Tolerant af', 'b. Moderate tolerance', 'c. Low tolerance', 'd. Frustration overload'],
    ['a. Joyful every day', 'b. Some joy here and there', 'c. Rarely joyful', 'd. Joy? What\'s that?'],
    ['a. Fresh and clean', 'b. Occasionally neglecting', 'c. Frequently neglecting', 'd. Hygiene who?'],
    ['a. Laser-focused', 'b. Okay-ish attention', 'c. Hard to focus', 'd. Attention span of a goldfish'],
    ['a. Feeling great', 'b. Occasionally doubtful', 'c. Frequently doubtful', 'd. Worthless vibes'],
    ['a. Thick-skinned', 'b. Handling it okay', 'c. Struggling with criticism', 'd. Criticism hurts'],
    ['a. Socializing pro', 'b. Here and there', 'c. Low motivation', 'd. Socializing? Nah.'],
    ['a. No changes', 'b. A bit up or down', 'c. Significant weight changes', 'd. Weight\'s a mystery'],
    ['a. Anxiety-free', 'b. A bit anxious', 'c. Frequently anxious', 'd. Anxiety overload'],
    ['a. Loving it', 'b. Some interest left', 'c. Lost interest', 'd. Work or studies? Nah.'],
    ['a. Decision-making guru', 'b. Decent decisions', 'c. Hard to decide', 'd. Decisions? Not today.'],
    ['a. Task master', 'b. Some tasks get done', 'c. Struggling to start tasks', 'd. Tasks? Never started.'],
    ['a. Enjoying it all', 'b. Some joy here and there', 'c. Rarely joyful', 'd. Joy? What\'s that?'],
    ['a. Motivated af', 'b. Moderate motivation', 'c. Low motivation', 'd. No motivation at all'],
    ['a. Engaged in every conversation', 'b. Okay-ish focus', 'c. Hard to focus on conversations', 'd. Conversations who?'],
    ['a. Lost in daydreams', 'b. Balanced between daydreaming and focus', 'c. Mostly focused on the present', 'd. Always fully focused'],
    ['a. Frequently', 'b. Sometimes', 'c. Rarely', 'd. Never'],
    ['a. Not satisfied at all', 'b. Somewhat satisfied', 'c. Fairly satisfied', 'd. Completely satisfied'],
    ['a. Rarely', 'b. Sometimes', 'c. Often', 'd. Daily'],
    ['a. Yes, frequently', 'b. Occasionally', 'c. Rarely', 'd. Never'],
    ['a. Easily discouraged', 'b. Somewhat resilient', 'c. Fairly resilient', 'd. Extremely resilient'],
    ['a. Not satisfied at all', 'b. Somewhat satisfied', 'c. Fairly satisfied', 'd. Completely satisfied'],
    ['a. Frequently', 'b. Sometimes', 'c. Rarely', 'd. Never'],
    ['a. Not confident at all', 'b. Somewhat confident', 'c. Fairly confident', 'd. Extremely confident'],
    ['a. Rarely', 'b. Sometimes', 'c. Often', 'd. Daily'],
]
option_list= [
    ["Refreshed and rejuvenated",
    "Decent with interruptions",
    "Struggled and tired",
    "Tossed and turned all night"],

    ["Light reading or music",
    "Warm bath or shower",
    "Meditation or breathing exercises",
    "Avoid screens before bed"],

    ["Full of energy",
    "Balanced throughout the day",
    "Alert in the evening",
    "Fatigue and low energy"],

    ["Whole foods and lean proteins",
    "Complex carbohydrates",
    "Healthy fats",
    "Quick snacks for energy"],

    ["Mindfulness and breathing exercises",
    "Regular exercise",
    "Hobbies and relaxation",
    "Seeking support from others"],

    ["Facial wipes or mists",
    "Dry shampoo",
    "Small toothbrush and toothpaste",
    "Natural deodorants"],

    ["Problem-solving tasks or puzzles",
    "Stimulating conversations",
    "Podcasts or audiobooks",
    "Short breaks for stretching or walking"],

    ["Planning meals and balanced nutrition",
    "Experimenting with new recipes",
    "Listening to hunger cues",
    "Variety and color on the plate"],

    ["Nutritious meals boost mood and energy",
    "Comfort foods for temporary mood boost",
    "Skipping meals leads to irritability",
    "Certain foods cause mood crashes"],

    ["Regular exercise including cardio and strength training",
    "Staying hydrated with water and electrolytes",
    "Listening to body's signals for rest",
    "Stress-reducing activities like yoga or stretching"],
    ["Upbeat and positive",
    "Mixed emotions, mostly content",
    "Struggling with low moods",
    "Feeling overwhelmed"],

    ["Mindfulness practices",
    "Nature walks",
    "Reading or watching",
    "Spending time with loved ones"],

    ["Calm and composed",
    "Embracing challenges",
    "Finding creative solutions",
    "Overwhelmed by challenges"],

    ["Setting ambitious goals",
    "Taking small steps",
    "Drawing inspiration from others",
    "Visualizing rewards"],

    ["Diving deep into tasks",
    "Efficient multitasking",
    "Structured work breaks",
    "Using techniques like Pomodoro"],

    ["Outdoor adventures",
    "Binge-watching",
    "Quality time with loved ones",
    "Exploring new hobbies"],

    ["Solitary activities",
    "Socializing with friends",
    "Self-care rituals",
    "Mindfulness exercises"],

    ["Meticulous planning",
    "Adapting on the fly",
    "Delegating tasks",
    "Flexible approach"],

    ["Luxurious pampering",
    "Simple daily routines",
    "Emotional nurturing",
    "Finding joy in simplicity"],

    ["Quick bounce back",
    "Reflective processing",
    "Seeking support",
    "Maintaining resilience"]
]


# In[4]:


scores = [
    [1, 0.75, 0.50, 0.25],  
    [1, 0.75, 0.50, 0.25],  
    [1, 0.75, 0.50, 0.25],  
    [1, 0.75, 0.50, 0.25],  
    [1, 0.75, 0.50, 0.25],  
    [1, 0.75, 0.50, 0.25],  
    [1, 0.75, 0.50, 0.25],  
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [1, 0.75, 0.50, 0.25],   
    [0.25, 0.50, 0.75, 1],   
    [0.25, 0.50, 0.75, 1],   
    [0.25, 0.50, 0.75, 1],   
    [0.25, 0.50, 0.75, 1],   
    [0.25, 0.50, 0.75, 1],   
    [0.25, 0.50, 0.75, 1],   
    [0.25, 0.50, 0.75, 1],   
    [0.25, 0.50, 0.75, 1],   
    [0.25, 0.50, 0.75, 1],   
    [0.25, 0.50, 0.75, 1],   
    [0.25, 0.50, 0.75, 1],   
]


# In[5]:


scores = [
    [1, 0.75, 0.50, 0.25], 
]


# In[6]:


def evaluate_user():
    selected_indices = random.sample(range(len(prompts)), 20)
    total_score = 0

    for index in selected_indices:
        print("\nQuestion:", prompts[index])
        options_to_display = option_list[index]
        random.shuffle(options_to_display)  # Shuffle options for randomness
        options_to_display = options_to_display[:4]  # Select only 4 options
        for i, option in enumerate(options_to_display):
            print(f"{chr(97 + i)}. {option}")
        user_choice = input("Your choice (a/b/c/d): ").strip().lower()

        if user_choice in ['a', 'b', 'c', 'd']:
            option_index = ord(user_choice) - ord('a')
            total_score += scores[0][option_index]
        else:
            print("Invalid choice. Skipping this question.")

        if index == selected_indices[-1]:
            break

    percentage_score = (total_score / 20) * 100
    print("\nTotal score:", total_score, "out of 20")
    print("Percentage score:", percentage_score)

    if percentage_score >= 80:
        print("Congratulations! You scored above 80%. You're doing well!")
    elif 60 <= percentage_score < 80:
        print("Your score is between 60% and 80%. Generating 5 additional questions.")
        generated_questions = generate_questions(prompts, 5)
        print_generated_questions(generated_questions)
    elif 40 <= percentage_score < 60:
        print("Your score is between 40% and 60%. Generating 7 additional questions.")
        generated_questions = generate_questions(prompts, 7)
        print_generated_questions(generated_questions)
    else:
        print("Your score is below 40%. Generating 10 additional questions.")
        generated_questions = generate_questions(prompts, 10)
        print_generated_questions(generated_questions)


# In[7]:


def generate_questions(prompts, num_questions):
    questions = []
    selected_indices = random.sample(range(len(prompts)), num_questions)
    for index in selected_indices:
        options_to_display = option_list[index]
        random.shuffle(options_to_display)  # Shuffle options for randomness
        options_to_display = options_to_display[:4]  # Select 4 options
        question = {
            "question": prompts[index],
            "options": options_to_display
        }
        questions.append(question)
    return questions


# In[8]:


def print_generated_questions(generated_questions):
    for i, question in enumerate(generated_questions):
        print(f"\nAdditional Question {i+1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{chr(97 + j)}. {option}")


# In[9]:


from transformers import T5ForConditionalGeneration, T5Tokenizer


# In[10]:


model_name = "t5-small"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)


# In[11]:


paragraph = "Normal sleep duration for typically around 8 hours per night. During the day, a normal man tends to feel alert, focused, and energetic, while at night, he feels tired and experiences a natural desire to sleep. In terms of diet and eating habits, a normal man generally maintains a balanced and nutritious diet, consuming regular meals throughout the day. He may occasionally indulge in unhealthy foods or skip meals, but these instances are not frequent or excessive. Additionally, he practices good hygiene, engages in regular physical activity, and manages stress effectively."


# In[12]:


# generated_questions = generate_questions(prompts, 10, option_list)


# In[13]:


evaluate_user()

