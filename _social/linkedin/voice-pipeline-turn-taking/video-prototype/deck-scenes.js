const DECK_SCENES = [
  {
    "type": "slide",
    "id": 1,
    "data": {
      "style": "statement",
      "lines": [
        "Talking to an AI can be",
        "genuinely powerful."
      ]
    }
  },
  {
    "type": "checklist",
    "id": 2,
    "kicker": "USE CASES",
    "items": [
      "Brainstorming on a walk",
      "Speaking instructions while vibe-coding",
      "Steering a robot — no keyboard to type on"
    ],
    "step": 1
  },
  {
    "type": "checklist",
    "id": 3,
    "kicker": "USE CASES",
    "items": [
      "Brainstorming on a walk",
      "Speaking instructions while vibe-coding",
      "Steering a robot — no keyboard to type on"
    ],
    "step": 2
  },
  {
    "type": "checklist",
    "id": 4,
    "kicker": "USE CASES",
    "items": [
      "Brainstorming on a walk",
      "Speaking instructions while vibe-coding",
      "Steering a robot — no keyboard to type on"
    ],
    "step": 3
  },
  {
    "type": "slide",
    "id": 5,
    "data": {
      "style": "pipeline-basic",
      "lines": []
    }
  },
  {
    "type": "slide",
    "id": 6,
    "data": {
      "style": "statement",
      "lines": [
        "This already exists as a streaming API",
        "you can just call."
      ]
    }
  },
  {
    "type": "slide",
    "id": 7,
    "data": {
      "style": "pipeline-cloud",
      "lines": []
    }
  },
  {
    "type": "slide",
    "id": 8,
    "data": {
      "style": "pipeline-local",
      "lines": []
    }
  },
  {
    "type": "slide",
    "id": 9,
    "data": {
      "style": "statement",
      "lines": [
        "A lot of that logic",
        "is on you."
      ]
    }
  },
  {
    "type": "slide",
    "id": 10,
    "data": {
      "style": "pause"
    }
  },
  {
    "type": "slide",
    "id": 11,
    "data": {
      "style": "statement",
      "lines": [
        "Wait for one big block of audio,",
        "and you're staring at silence."
      ]
    }
  },
  {
    "type": "slide",
    "id": 12,
    "data": {
      "style": "statement",
      "lines": [
        "So instead: chunk it,",
        "keep re-transcribing in the background."
      ]
    }
  },
  {
    "type": "diagram",
    "id": 13,
    "step": 1,
    "group": "chunk_transcribe"
  },
  {
    "type": "diagram",
    "id": 14,
    "step": 2,
    "group": "chunk_transcribe"
  },
  {
    "type": "diagram",
    "id": 15,
    "step": 3,
    "group": "chunk_transcribe"
  },
  {
    "type": "diagram",
    "id": 16,
    "step": 4,
    "group": "chunk_transcribe"
  },
  {
    "type": "diagram",
    "id": 17,
    "step": 5,
    "group": "chunk_transcribe"
  },
  {
    "type": "slide",
    "id": 18,
    "data": {
      "style": "statement",
      "lines": [
        "Now the LLM needs to be fast too.",
        "This is where VAD actually comes in."
      ]
    }
  },
  {
    "type": "diagram",
    "id": 19,
    "step": 1,
    "group": "pipeline_speculative"
  },
  {
    "type": "diagram",
    "id": 20,
    "step": 2,
    "group": "pipeline_speculative"
  },
  {
    "type": "diagram",
    "id": 21,
    "step": 3,
    "group": "pipeline_speculative"
  },
  {
    "type": "diagram",
    "id": 22,
    "step": 4,
    "group": "pipeline_speculative"
  },
  {
    "type": "diagram",
    "id": 23,
    "step": 5,
    "group": "pipeline_speculative"
  },
  {
    "type": "diagram",
    "id": 24,
    "step": 6,
    "group": "pipeline_speculative"
  },
  {
    "type": "diagram",
    "id": 25,
    "step": 7,
    "group": "pipeline_speculative"
  },
  {
    "type": "diagram",
    "id": 26,
    "step": 8,
    "group": "pipeline_speculative"
  },
  {
    "type": "diagram",
    "id": 27,
    "step": 9,
    "group": "pipeline_speculative"
  },
  {
    "type": "diagram",
    "id": 28,
    "step": 10,
    "group": "pipeline_speculative"
  },
  {
    "type": "slide",
    "id": 29,
    "data": {
      "style": "statement",
      "lines": [
        "Don't wait for the full reply either.",
        "Stream tokens straight into speech."
      ]
    }
  },
  {
    "type": "slide",
    "id": 30,
    "data": {
      "style": "thesis",
      "lines": [
        "Fast conversation.",
        "Bad for thinking out loud."
      ],
      "kicker": "HUGGINGFACE REAL-TIME PIPELINE"
    }
  },
  {
    "type": "slide",
    "id": 31,
    "data": {
      "style": "statement",
      "lines": [
        "I manually decide when to hand the turn over —",
        "and run my own agent, not a general-purpose one."
      ]
    }
  },
  {
    "type": "diagram",
    "id": 32,
    "step": 1,
    "group": "pipeline_steps"
  },
  {
    "type": "diagram",
    "id": 33,
    "step": 2,
    "group": "pipeline_steps"
  },
  {
    "type": "diagram",
    "id": 34,
    "step": 3,
    "group": "pipeline_steps"
  },
  {
    "type": "diagram",
    "id": 35,
    "step": 4,
    "group": "pipeline_steps"
  },
  {
    "type": "diagram",
    "id": 36,
    "step": 5,
    "group": "pipeline_steps"
  },
  {
    "type": "diagram",
    "id": 37,
    "step": 6,
    "group": "pipeline_steps"
  },
  {
    "type": "diagram",
    "id": 38,
    "step": 7,
    "group": "pipeline_steps"
  },
  {
    "type": "diagram",
    "id": 39,
    "step": 8,
    "group": "pipeline_steps"
  },
  {
    "type": "diagram",
    "id": 40,
    "step": 9,
    "group": "pipeline_steps"
  },
  {
    "type": "diagram",
    "id": 41,
    "step": 10,
    "group": "pipeline_steps"
  },
  {
    "type": "slide",
    "id": 42,
    "data": {
      "style": "wakeword",
      "lines": []
    }
  },
  {
    "type": "slide",
    "id": 43,
    "data": {
      "style": "bargein-interrupt",
      "lines": []
    }
  },
  {
    "type": "slide",
    "id": 44,
    "data": {
      "style": "bargein-button",
      "lines": []
    }
  },
  {
    "type": "slide",
    "id": 45,
    "data": {
      "style": "echo-overlap",
      "lines": []
    }
  },
  {
    "type": "slide",
    "id": 46,
    "data": {
      "style": "echo-compare",
      "lines": []
    }
  },
  {
    "type": "slide",
    "id": 47,
    "data": {
      "style": "wakeword-mini",
      "lines": []
    }
  },
  {
    "type": "slide",
    "id": 48,
    "data": {
      "style": "statement",
      "lines": [
        "I wrote the whole walkthrough down."
      ]
    }
  },
  {
    "type": "slide",
    "id": 49,
    "data": {
      "style": "cta",
      "kicker": "FULL WRITEUP AND WALKTHROUGH",
      "content": "quantitative-thinking.com"
    }
  }
];
