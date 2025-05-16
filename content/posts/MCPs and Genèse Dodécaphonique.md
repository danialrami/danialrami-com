---
title: MCPs and Genese Dodecaphonique
date: 2025-05-16
draft: false
---
## Introduction

As a sound designer working across various digital audio workstations and interactive media, I've always been fascinated by the intersection of music theory, technology, and creative workflows. Years ago, as a student of the renowned French composer Michel Merlet, I was introduced to his unique theoretical framework called "Genèse Dodécaphonique des Modes" – a systematic approach to understanding modal structures within the twelve-tone system. This framework has profoundly influenced my approach to composition and sound design over the years.

Today, we stand at an exciting crossroads where large language models (LLMs) are transforming creative workflows across disciplines. In this post, I'll demonstrate how sound designers can leverage custom LLM tools to bridge theoretical musical concepts with practical applications, using Merlet's modal system as a concrete example.

## The Merlet System Explained

The "Genèse Dodécaphonique des Modes" (Dodecaphonic Genesis of Modes) is Michel Merlet's systematic approach to categorizing and understanding various modal structures within the twelve-tone musical system. Unlike conventional classifications, Merlet's system organizes modes based on their mathematical properties, symmetrical characteristics, and historical usage.

The system is visually represented as a clock-like circular diagram, with the twelve chromatic tones arranged around the perimeter. Each mode is color-coded and radiates from the center, creating a visual map of tonal relationships:

![Image Description](/images/attachments/MusicChart_120120v2.jpg)
*Shoutout to [Ash Suh](https://ashsuh.com/) for making this copy for me, many years ago!*

The modes are numbered from 0 to 12:

**Mode 0: Chromatic (12-12=0)**  
The complete chromatic scale using all twelve tones. It has no complementary structure ("absence de complémentarité") and is historically exemplified in Schoenberg's "Valse, Cinq pièces opus 23" (1923).

**Mode 1: Triton**  
Based on the tritone interval (6 semitones), creating an "antipodal" symmetry that divides the octave precisely in half. Historically referenced in Ballif's "À cor et à cri" (1962).

**Mode 2: 8÷2=5 (Diminished)**  
Created with consistent 2-semitone intervals, producing a symmetrical diminished structure. Exemplified in Messiaen's "4e partie de l'Ascension" (1933).

**Mode 3: 8÷3=8/3 (Augmented)**  
Based on consistent 4-semitone intervals (major thirds), creating a perfectly symmetrical augmented structure. Found in Messiaen's "Thème et variations" (1932).

**Mode 4: 8÷4=7**  
A symmetrical mode built on 3-semitone jumps, as used in Stravinsky's "Symphonie des psaumes" (1930).

**Mode 5: Pentatonic**  
The asymmetrical five-note scale, historically referenced in Fauré's "Fantaisie pour piano et orchestre" (1919).

**Mode 6: Par tons (Whole Tone)**  
Composed of consistent whole-tone intervals (2 semitones), creating perfect symmetry. Exemplified in Debussy's "Voiles" from his first book of Preludes (1910).

**Mode 7: Diatonic**  
The traditional seven-note scale (like major and minor scales) with its characteristic asymmetrical pattern of whole and half steps. Referenced in Ravel's "La décronnelle" (1908).

The diagram also shows modes 8-12, which complement modes 4-0 respectively, creating a symmetrical relationship within the system.

What makes Merlet's system particularly valuable is how it connects mathematical properties with historical compositions, demonstrating that these structures aren't merely theoretical but have been intuitively discovered and employed by composers throughout the 20th century. My favorite part is how it recontextualizes tonal music away from the traditional Greek modes and begins with a simple notion -- "let's start with the octave, and keep splitting evenly."

## LLM Tools & Model Context Protocols (MCPs)

Large Language Models have evolved beyond simple text generation into powerful assistants that can extend their capabilities through tools - specialized programs that perform specific functions when called by the LLM. These tools enable LLMs to perform calculations, retrieve information, or generate specialized content outside their training parameters.

Model Context Protocols (MCPs) represent the next evolution in this ecosystem - standardized ways for LLMs to interact with external tools, data sources, and computation engines. Unlike one-off custom tools, MCPs provide a framework for developers to create consistent, reusable interfaces between models and external systems.

For creative fields like sound design and music composition, MCPs hold particular promise. Musical concepts often exist in a space between abstract theory and concrete implementation - MCPs can bridge this gap by allowing LLMs to reason about musical structures while connecting to the tools that actually produce or manipulate sound.

## Case Study: Building a Merlet Mode Generator Tool

To demonstrate this concept, I created a custom LLM tool that generates Merlet modes for any given root note. This Python-based tool encapsulates the theoretical framework while making it immediately applicable to compositional work.

Here's the core functionality of the tool:

```python
def generate_merlet_modes(root_note="C"):
    notes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    # Define all modes from Merlet's diagram
    modes = [
        Mode(
            0,
            "12-12=0 Chromatic",
            [1] * 12,
            SymmetryType.NONE,
            HistoricalReference("Schönberg", "Valse, Cinq pièces opus 23", 1923),
        ),
        # Additional modes defined here...
    ]
    
    # Generate scales for each mode starting with the specified root note
    results = []
    for mode in modes:
        primary_scale = generate_scale(mode.intervals, start_index)
        complement_scale = [note for note in notes if note not in primary_scale]
        results.append(
            {
                "mode_number": mode.number,
                "name": f"Mode {mode.number}: {mode.name}",
                "symmetry": mode.symmetry_type.value,
                "primary": primary_scale,
                "complement": complement_scale,
                "historical_ref": f"{mode.historical_ref.composer} - {mode.historical_ref.work} ({mode.historical_ref.year})",
            }
        )
    return results
```

I integrated this tool with OpenWebUI, allowing me to interact with it through natural language. For example, I prompt:

> "Generate the Merlet table in markdown format with root note C"

And receive a comprehensive table showing each mode, its symmetry properties, scale notes, complementary notes, and historical reference:

|Mode|Symmetry|Primary Scale|Complementary Scale|Historical Reference|
|---|---|---|---|---|
|Mode 0: 12-12=0 Chromatic|absence de complémentarité|C Db D Eb E F Gb G Ab A Bb B||Schönberg - Valse, Cinq pièces opus 23 (1923)|
|Mode 1: Triton|antipodal|C Gb|Db D Eb E F G Ab A Bb B|Ballif - À cor et à cri (1962)|
|Mode 2: 8÷2-5|symmetric|C D E Gb|Db Eb F G Ab A Bb B|Messiaen - 4e partie de l'Ascension (1933)|
|...|...|...|...|...|

## Applications for Sound Designers

The implications for sound design go beyond mere academic interest. By encoding Merlet's theoretical framework into an accessible tool, we open up several practical applications:

### 1. Compositional Frameworks

Using these modal structures as starting points for compositions ensures coherence while exploring beyond conventional tonality. Each mode has its distinct emotional character and historical context, providing creative direction.

### 2. Sound Design Parameters

The symmetrical properties of these modes can inform synthesizer parameter settings. For example:

- Using Mode 3's augmented structure to create equidistant filter modulations
- Applying Mode 4's symmetrical intervals to FM synthesis ratios
- Mapping Mode 6's whole-tone structure to granular density parameters

### 3. Generative Audio Systems

Algorithmic composition systems can leverage these well-defined modal structures as rule sets, particularly in adaptive game audio where tonal consistency must be maintained across procedurally generated content.

### 4. Timbral Exploration

The complementary structure of Merlet's system (where each mode has its complement) provides a framework for designing contrasting but related timbres—useful for creating coherent soundscapes with internal variation.

## MCP Integration for Audio Applications

While my current implementation works as a standalone tool in OpenWebUI, the real potential lies in developing dedicated Model Context Protocol servers for audio manipulation. Here's how this could evolve:

### Audio-Specific MCP Server

An audio-focused MCP server could provide LLMs with direct control over:

1. **Scale-Based Synthesis** - Generate synthesizer patches based on modal characteristics
2. **Real-time Audio Analysis** - Analyze recorded audio for its modal content
3. **DAW Integration** - Send MIDI data or control parameters directly to digital audio workstations
4. **Sample Retrieval and Manipulation** - Find and transform audio samples to match specific modal characteristics

### Example Interaction

Imagine prompting an LLM with:

> "Create an evolving pad sound based on Merlet's Mode 3 with increasing tension over 16 bars, export as MIDI and send parameter automation to my instance of Vital synth"

The MCP server would:

1. Generate the Mode 3 scale structure (C E Ab)
2. Create MIDI patterns emphasizing these notes
3. Design synthesis parameters that accentuate the equidistant nature of the augmented scale
4. Program automation curves that increase complexity over time
5. Export directly to your DAW or synth

This level of integration would transform how we approach sound design, bridging the gap between theoretical concepts and practical implementation.

## Conclusion

The marriage of specialized musical knowledge with the emerging capabilities of LLMs and Model Context Protocols represents a new frontier for sound designers. By building custom tools that encapsulate theoretical frameworks like Merlet's modal system, we can make complex musical concepts immediately applicable to our creative workflows.

As we continue to develop these integrations, the boundary between conceptual thinking and implementation will become increasingly fluid. Sound designers will be able to move seamlessly between high-level musical ideas and their concrete sonic realizations, opening new possibilities for creative exploration.

I invite fellow sound designers to experiment with custom LLM tools and contribute to the development of audio-focused MCPs. The code for my Merlet Mode Generator is available at [repository link], and I welcome collaboration on extending its capabilities.

---

_What innovative ways are you using LLMs in your sound design workflow? I'd love to hear your thoughts and experiences in the comments below._