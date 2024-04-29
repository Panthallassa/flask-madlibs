from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, )
"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

# The fairytale
story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
# The Mysterious Forest
story2 = Story(
    ["place", "noun", "verb", "place", "adjective"],
    """In a {place} far away, there lived a lonely {noun}. 
    Every day, it would {verb}, around the {place}, 
    searching for {adjective} things to eat."""
)
# The Enchanted Garden
story3 = Story(
    ["noun", "adjective", "verb", "plural_noun"],
    """The {noun} in the {adjective} garden liked to {verb} and play.
    They would gather their {plural_noun} and explore the
    magical world around them."""
)
# The Haunted Mansion
story4 = Story(
    ["place", "adjective", "plural_noun", "verb"],
    """Deep in the {place}, there was a mansion rumored to be
    {adjective}. Many {plural_noun} claimed to have seen ghosts
    {verb} around the old house at night."""
)
# The Lost City
story5 = Story(
    ["adjective", "verb", "noun"],
    """The {adjective} city was hidden deep within the jungle.
    Explorers would {verb} for days, hoping to find the ancient
    {noun} that held the secrets of the past."""
)
# The Wandering Traveller
story6 = Story(
    ["place", "adjective", "plural_noun", "noun"],
    """In the {place}, of Azura, there stood a {adjective} tower
    that stretched into the sky. Legend had it that at the top 
    of the tower, one could hear the {plural_noun} of the winds
    whispering ancient tales of {noun}."""
)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/start_story', methods=['GET','POST'])
def start_story():
        selected_story = request.form.get('selected_story')
        if selected_story:
            return redirect(url_for(selected_story))
        else:
            return render_template('home.html')

@app.route('/story1', methods=['GET','POST'])
def story_1():
    if request.method == 'POST':
        inputs = {prompt: request.form[prompt] for prompt in ["place", "noun", "verb", "adjective", "plural_noun"]}

        generated_story = story1.generate(inputs)

        return redirect(url_for('generate_story', story=generated_story))
    else:
        return render_template('story_form1.html')
    
@app.route('/story2', methods=['GET', 'POST'])
def story_2():
    if request.method == 'POST':
        inputs = {prompt: request.form[prompt] for prompt in ["place", "noun", "verb", "adjective", "place"]}

        generated_story = story2.generate(inputs)

        return redirect(url_for('generate_story', story=generated_story))
    else:
        return render_template('story_form2.html')
    
@app.route('/story3', methods=['GET', 'POST'])
def story_3():
    if request.method == 'POST':
        inputs = {prompt: request.form[prompt] for prompt in ["noun", "verb", "adjective", "plural_noun"]}

        generated_story = story3.generate(inputs)

        return redirect(url_for('generate_story', story=generated_story))
    else:
        return render_template('story_form3.html')
    
@app.route('/story4', methods=['GET', 'POST'])
def story_4():
    if request.method == 'POST':
        inputs = {prompt: request.form[prompt] for prompt in ["place", "verb", "adjective", "plural_noun"]}

        generated_story = story4.generate(inputs)
        
        return redirect(url_for('generate_story', story=generated_story))
    else:
        return render_template('story_form4.html')
    
@app.route('/story5', methods=['GET', 'POST'])
def story_5():
    if request.method == 'POST':
        inputs = {prompt: request.form[prompt] for prompt in ["noun", "verb", "adjective"]}

        generated_story = story5.generate(inputs)

        return redirect(url_for('generate_story', story=generated_story))
    else:
        return render_template('story_form5.html')
    
@app.route('/story6', methods=['GET', 'POST'])
def story_6():
    if request.method == 'POST':
        inputs = {prompt: request.form[prompt] for prompt in ["place", "noun", "adjective", "plural_noun"]}

        generated_story = story6.generate(inputs)

        return redirect(url_for('generate_story', story=generated_story))
    else:
        return render_template('story_form6.html')
    
@app.route('/generate_story')
def generate_story():
    generated_story = request.args.get('story')

    return render_template('generate_story.html', story=generated_story)
