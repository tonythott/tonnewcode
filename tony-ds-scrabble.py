{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Scrabble Program"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "import string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "consonants = \"bcdfghjklmnpqrstvwxyz\"\n",
    "vowels = \"aeiou\"\n",
    "num_letters = 7\n",
    "\n",
    "min_vowels = 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [],
   "source": [
    "scores = {'A': 1, 'C': 3, 'B': 3, 'E': 1, 'D': 2, 'G': 2, 'F': 4, 'I': 1, 'H': 4, 'K': 5, 'J': 8, 'M': 3, 'L': 1, 'O': 1, 'N': 1, 'Q': 10, 'P': 3, 'S': 1, 'R': 1, 'U': 1, 'T': 1, 'W': 4, 'V': 4, 'Y': 4, 'X': 8, 'Z': 10}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "# load the words\n",
    "\n",
    "import zipfile\n",
    "\n",
    "words = []\n",
    "with zipfile.ZipFile(\"words.zip\") as z:\n",
    "    with z.open(\"words.txt\") as f:\n",
    "        for line in f:\n",
    "            words.append(line.strip().decode().upper())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "# validate function\n",
    "\n",
    "def validate(current_hand, word):\n",
    "    \n",
    "    # check if user entered \"end\", return \"End\"\n",
    "    # VONG\n",
    "    if debug == True:\n",
    "        print(\"word in validate function\",word)\n",
    "    if word == '.':\n",
    "        return ('End',None)\n",
    "    \n",
    "    # check of word can be formed with the current hand\n",
    "    # if new hand cannot be formed return \"Insufficient Letters\"\n",
    "    hand = list(current_hand)\n",
    "    for letter in list(word):\n",
    "        if letter in hand:\n",
    "            hand.remove(letter)\n",
    "        else:\n",
    "            return (\"Insufficient Letters\", None)\n",
    "        \n",
    "    new_hand = \"\".join(hand)\n",
    "    \n",
    "    # check if word is present in dictionary\n",
    "    if word.upper() in words:\n",
    "        return (\"Found\", new_hand)\n",
    "    else:\n",
    "        return (\"Word Not Found\",None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [],
   "source": [
    "# update score\n",
    "\n",
    "def update_score(current_score,word):\n",
    "    \n",
    "    score = 0\n",
    "    for char in word.upper():\n",
    "        score += scores[char]\n",
    "        \n",
    "    current_score = current_score + score\n",
    "    \n",
    "    return current_score "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [],
   "source": [
    "# distribute the initial hand\n",
    "import random\n",
    "import numpy as np\n",
    "\n",
    "def initial_hand():\n",
    "    \n",
    "    hand = []\n",
    "    \n",
    "    # get vowels\n",
    "    for i in np.arange(min_vowels):\n",
    "        letter = random.choice(vowels)\n",
    "        hand.append(letter)\n",
    "    \n",
    "    # get remaining letters\n",
    "    for i in np.arange(num_letters-min_vowels):\n",
    "        letter = random.choice(string.ascii_lowercase)\n",
    "        hand.append(letter)\n",
    "                           \n",
    "    return \"\".join(hand)\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Main Program"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current score: 0\n",
      "Initial hand: eoyyxze\n",
      "\n",
      "***Enter . to end the game or enter a word***\n",
      "Please create a word:eye\n",
      "\n",
      "Remaining Letters:oyxz, New Score:6\n",
      "\n",
      "***Enter . to end the game or enter a word***\n",
      "Please create a word:ox\n",
      "\n",
      "Remaining Letters:yz, New Score:15\n",
      "\n",
      "***Enter . to end the game or enter a word***\n",
      "Please create a word:.\n",
      "\n",
      "Final Score:15\n",
      "Bye Bye\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "debug = False\n",
    "\n",
    "# initialize current score\n",
    "current_score = 0\n",
    "current_hand = initial_hand()\n",
    "\n",
    "print(\"Current score:\",current_score)\n",
    "print(\"Initial hand:\",current_hand)\n",
    "sys.stdout.flush()\n",
    "\n",
    "while True:\n",
    "    \n",
    "    print(\"\\n***Enter . to end the game or enter a word***\")\n",
    "\n",
    "    # request user to form a word\n",
    "    word = input(\"Please create a word:\")\n",
    "\n",
    "    # validate the word\n",
    "    valid_string, new_hand = validate(current_hand,word)\n",
    "    \n",
    "    if valid_string == \"Insufficient Letters\":\n",
    "        print(\"Insufficient Letters. Try again...\")\n",
    "        continue\n",
    "        \n",
    "    if debug == True:\n",
    "        print(\"valid_string right before check for End\",valid_string)\n",
    "        \n",
    "    if valid_string == \"End\":\n",
    "        print(\"\\nFinal Score:%d\" % (current_score))\n",
    "        print(\"Bye Bye\")\n",
    "        break\n",
    "\n",
    "    if valid_string == \"Word Not Found\":\n",
    "        print(\"Word not Found. Try again...\")\n",
    "        continue\n",
    "        \n",
    "    # update the hand\n",
    "    current_hand = new_hand\n",
    "        \n",
    "    # update the score\n",
    "    current_score = update_score(current_score, word)\n",
    "\n",
    "    print(\"\\nRemaining Letters:%s, New Score:%d\" % (new_hand,current_score))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}