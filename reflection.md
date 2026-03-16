# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the hints were backwards").
=======
  (for example: "the secret number kept changing" or "the hints were backwards").
  When the game first started, the hints were not only backwards, but everytime I tried to start a new game after winning, it just would not let me. When I tried to answer lower, sometimes it would give me a hint that was way off, that ended up derailing my attempts at solving the game instead of being accurate and helping me. When I would try to start a new game, the new game button just would not work, instead of actually starting a new game. There was also some hard coding when it came to the difficulty. I also found that the difficulty levels were off along with the rounding of various variables. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI tools I used were Claude and GitHub Copilot. One suggestion given to me by GitHub Copilot that was correct was changing the parse_guess method to round a variable instead of flooring them, which gave better guesses over all, which I verified by testing 9.9 and 3.1 and then checking the debug menu to see what they turned out was. Another suggestion given to me by Claude AI Opus 4.6 that was incorrect/misleading was removing the if-else statement where we assign secret, which I verified by trying to play the game (and failing). I fixed this issue by making secret autoamtically be assigned when the submit button was clicked. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I would first check any base cases relating to the bug, then begin to test any edge cases. One test I ran was a pytest where I made sure the hints worked, by testing four edge cases for the hardest difficulty. AI helped me design the test by creating the pytest, and it gave me the commands necessary to run them. This was helpful since I've been a bit rusty with my pytests. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns are equivalent to typing on your keyboard, and the session state is just your screen after each key is typed. This is because reruns directly affect the session states, even misclicks, or in the example's case, typing errors. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One habit I learned from this project I plan on reusing is having AI point out the errors for me, since they did steamline my process by a lot. One thing I would do more differently is have my AI be a lot more concise when giving explanations as I felt I had to still constantly change my code no matter what. This project changed the way I thought about AI generated code by making me realize that it isn't too bad.