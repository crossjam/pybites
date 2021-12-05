import string
import re

from collections import Counter
from dataclasses import dataclass, field
from typing import List, Set, Tuple

STOPWORDS: set = {
    "she's",
    "wasn",
    "through",
    "won",
    "that'll",
    "his",
    "once",
    "this",
    "you",
    "ll",
    "has",
    "because",
    "m",
    "ours",
    "doing",
    "any",
    "aren't",
    "they",
    "shouldn't",
    "being",
    "out",
    "is",
    "our",
    "it",
    "don",
    "had",
    "nor",
    "your",
    "she",
    "you've",
    "themselves",
    "or",
    "y",
    "needn",
    "on",
    "to",
    "at",
    "it's",
    "ve",
    "s",
    "too",
    "up",
    "didn't",
    "during",
    "haven",
    "can",
    "haven't",
    "each",
    "couldn",
    "isn't",
    "not",
    "against",
    "where",
    "was",
    "aren",
    "all",
    "by",
    "why",
    "hers",
    "theirs",
    "have",
    "as",
    "yourself",
    "their",
    "very",
    "who",
    "yourselves",
    "over",
    "and",
    "again",
    "do",
    "weren't",
    "which",
    "ma",
    "in",
    "such",
    "herself",
    "yours",
    "doesn",
    "if",
    "my",
    "after",
    "into",
    "just",
    "now",
    "isn",
    "itself",
    "between",
    "will",
    "other",
    "its",
    "these",
    "should",
    "re",
    "below",
    "having",
    "am",
    "both",
    "d",
    "you'll",
    "but",
    "should've",
    "won't",
    "himself",
    "shan't",
    "the",
    "me",
    "weren",
    "further",
    "until",
    "here",
    "myself",
    "whom",
    "were",
    "hasn",
    "don't",
    "wouldn't",
    "been",
    "before",
    "above",
    "he",
    "than",
    "most",
    "shan",
    "them",
    "mustn't",
    "couldn't",
    "you'd",
    "for",
    "of",
    "her",
    "those",
    "needn't",
    "you're",
    "t",
    "hadn't",
    "down",
    "o",
    "did",
    "about",
    "from",
    "does",
    "wouldn",
    "off",
    "then",
    "ain",
    "few",
    "hasn't",
    "some",
    "i",
    "ourselves",
    "an",
    "when",
    "are",
    "under",
    "more",
    "with",
    "hadn",
    "what",
    "while",
    "didn",
    "doesn't",
    "only",
    "him",
    "mightn",
    "be",
    "mightn't",
    "a",
    "how",
    "no",
    "there",
    "that",
    "so",
    "we",
    "same",
    "mustn",
    "wasn't",
    "shouldn",
    "own",
}
GETTYSBURG: str = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battlefield of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we cannot dedicate—we cannot consecrate—we cannot hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom— and that government of the people, by the people, for the people, shall not perish from the earth."""  # noqa E501


@dataclass
class Corpora:
    """Add the initial variables along with creating any methods that
    will get this working as described in the bite's description.

    * txt
    * count
    * tag
    * extra
    * stopwords
    """

    txt: str
    extra: List[str] = field(default_factory=list)
    stopwords: Set[str] = field(default_factory=set)
    count: int = 5
    tag: str = "#"

    def __post_init__(self):
        self.stopwords = STOPWORDS
        self.txt += " "

    @property
    def cleaned(self) -> str:
        """Takes a corpus and cleans it up.

        * All text is made lowercase
        * All punctuation is removed
        * If a list of extra characters were given, remove those too

        :param txt: Corpus of text
        :return: cleaned up corpus
        """
        # transmap = str.maketrans({c: None for c in string.punctuation})
        transmap = str.maketrans("", "", string.punctuation)
        transmap[8212] = " "
        # transmap.update({c: None for c in extra})
        nopunc_txt = self.txt.lower().translate(transmap).replace("\n", " ")
        # nopunc_txt = nopunc_txt.translate(transmap)
        # nopunc_txt = nopunc_txt.replace("\n", " ")
        for w in self.extra:
            nopunc_txt = nopunc_txt.replace(w, "")
        return nopunc_txt

    @property
    def metrics(self) -> List[Tuple[str, int]]:
        """Generates word count metrics.

        * Using the cleaned up corpus, count up how many times each word is used
        * Exclude stop words using STOPWORDS
        * Use count to return the requested amount of the top words, defaults to 5

        :return: List of tuples, i.e. ("word", count)
        """
        counts = Counter([w for w in self.cleaned.split() if w not in self.stopwords])
        counts.update([w[:3] for w in self.cleaned.split() if w == "mans"])
        return counts.most_common(self.count)

    @property
    def graph(self) -> None:
        """Generates a textual graph of the words

        * Prints out the words along with a "tag" bar graph, defaults to using
          the # character
        * The word is right-aligned and takes up 10 character spaces
        * The tag is repeated the number of counts of the word

        For example, the top 10 words in the Gettysburg address would be
        displayed in this manner:

            nation #####
         dedicated ####
             great ###
            cannot ###
              dead ###
                us ###
             shall ###
            people ###
               new ##
         conceived ##

        :param metrics: List of tuples with word counts
        :return: None
        """

        for w, count in self.metrics:
            print(f"{w:>10} {self.tag * count}")


if __name__ == "__main__":
    gettysburg = Corpora(GETTYSBURG)
    print(gettysburg.cleaned)
    print(len(GETTYSBURG))
    print(len(gettysburg.cleaned))
    gettysburg.count = 10
    print(gettysburg.metrics)
    gettysburg.graph
