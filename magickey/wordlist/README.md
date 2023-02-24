# Word Lists

Lists of words tp construct mnemonic phrases.  Ideally we should have around 7k of words, first names, last names.
To be able to encode 16 bits per word. Then First Name / Last Name : Word can be used to map into Ipv4 space/port.

An alternative BIP39 mapping can also be used, but discouraged. 

## Prompts

```
Please, can I have a few first names, starting with Ap, positive characters, ideally with a bit of association with sci-fi/fantasy/magic/pixar/tolkien/king arthur legends/zelazny amber?  Please avoid using variations of the same first name.  I'd like to use these names to construct mnemonic phrases.  Ideally these names should map directly onto your (LLM) tokens, please use names that are distinctive and easy for you to use.
```

```
Please, can I have these simply as words separated by a single space, instead of a list?  And again starting with letter K, not too negative, ideally with a bit of association with sci-fi/fantasy/magic/pixar/tolkien/king arthur legends/zelazny amber?  Please avoid using variations of the same word.  I'd like to use these words to construct mnemonic phrases.  Please, don't repeat the same word.   Output as words, separated by a single space, like this: Bed Bubble Banner Bolt

Please, can you make as a few hundred of these (starting with letter K) or as many as you can fit into a single answer?  To fill a page of a book in small letters?  Ideally these words should map directly onto your (LLM) tokens, please use words that are distinctive and easy for you to use. 
```