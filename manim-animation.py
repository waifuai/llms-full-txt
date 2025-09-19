"""
LLMs-Full.txt Generator Animation

This script creates an animated presentation using Manim to demonstrate the LLMs-Full.txt
Generator project. The animation showcases the project's purpose, structure, workflow,
and key features in an engaging visual format.

Animation Structure:
- Title and project overview introduction
- Visual representation of project structure with interconnected components
- Step-by-step workflow demonstration showing how the system works
- Key features highlight with animated bullet points
- Final summary and licensing information

Key Features:
- Professional animated presentation suitable for demos and documentation
- Visual breakdown of project components and their relationships
- Animated workflow showing the 4-step process
- Comprehensive feature showcase
- Smooth transitions and professional styling

Usage:
    manim -pql manim-animation.py LLMsFullTxtAnimation

Requirements:
    - Manim Community edition installed
    - Run from project root directory
    - Output video file will be generated in media/videos/

This animation serves as both a demonstration tool and educational content about the
project's capabilities and architecture.
"""

from manim import *

class LLMsFullTxtAnimation(Scene):
    def construct(self):
        # Title scene
        title = Text("LLMs-Full.txt Generator", font_size=48, color=BLUE)
        subtitle = Text("Making Project Documentation Accessible to AI", font_size=32, color=TEAL)
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Project overview
        overview_title = Text("Project Overview", font_size=40, color=YELLOW)
        overview_content = VGroup(
            Text("• Aggregates project documentation into one file", font_size=24),
            Text("• Makes content accessible to Large Language Models", font_size=24),
            Text("• Complements sitemap.xml and robots.txt", font_size=24),
            Text("• Uses Markdown format for AI-friendly structure", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        overview_content.next_to(overview_title, DOWN, buff=0.8)
        overview_title.move_to(UP*2)

        self.play(Write(overview_title))
        for line in overview_content:
            self.play(FadeIn(line))
        self.wait(3)
        self.play(FadeOut(overview_title), FadeOut(overview_content))

        # Project structure visualization
        structure_title = Text("Project Structure", font_size=40, color=GREEN)

        # Create boxes for each component
        src_box = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.2)
        src_label = Text("src/", font_size=24).move_to(src_box.get_center())

        utils_box = Rectangle(width=2.5, height=1, color=TEAL, fill_opacity=0.2)
        utils_label = Text("utils.py", font_size=20).move_to(utils_box.get_center())

        generate_llms_box = Rectangle(width=3, height=1, color=PURPLE, fill_opacity=0.2)
        generate_llms_label = Text("generate_llms.py", font_size=20).move_to(generate_llms_box.get_center())

        count_lines_box = Rectangle(width=3, height=1, color=ORANGE, fill_opacity=0.2)
        count_lines_label = Text("count_lines_of_code.py", font_size=18).move_to(count_lines_box.get_center())

        count_chars_box = Rectangle(width=3, height=1, color=RED, fill_opacity=0.2)
        count_chars_label = Text("count_chars_of_code.py", font_size=18).move_to(count_chars_box.get_center())

        generate_toc_box = Rectangle(width=3, height=1, color=PINK, fill_opacity=0.2)
        generate_toc_label = Text("generate_toc.py", font_size=20).move_to(generate_toc_box.get_center())

        tests_box = Rectangle(width=2.5, height=1, color=YELLOW, fill_opacity=0.2)
        tests_label = Text("tests/", font_size=20).move_to(tests_box.get_center())

        # Arrange the structure
        structure_title.move_to(UP*3)

        # Position src box in center
        src_box.move_to(UP*0.5)
        src_label.move_to(src_box.get_center())

        # Position utils and tests below src
        utils_box.move_to(DOWN*1 + LEFT*2)
        utils_label.move_to(utils_box.get_center())

        tests_box.move_to(DOWN*1 + RIGHT*2)
        tests_label.move_to(tests_box.get_center())

        # Position main scripts around
        generate_llms_box.move_to(UP*0.5 + LEFT*4)
        generate_llms_label.move_to(generate_llms_box.get_center())

        count_lines_box.move_to(UP*0.5 + RIGHT*4)
        count_lines_label.move_to(count_lines_box.get_center())

        count_chars_box.move_to(DOWN*2.5 + LEFT*2)
        count_chars_label.move_to(count_chars_box.get_center())

        generate_toc_box.move_to(DOWN*2.5 + RIGHT*2)
        generate_toc_label.move_to(generate_toc_box.get_center())

        # Create arrows
        arrows = VGroup()
        arrow_positions = [
            (src_box.get_right(), utils_box.get_left()),
            (src_box.get_right(), tests_box.get_left()),
            (src_box.get_left(), generate_llms_box.get_right()),
            (src_box.get_left(), count_lines_box.get_right()),
            (utils_box.get_top(), count_chars_box.get_bottom()),
            (tests_box.get_top(), generate_toc_box.get_bottom()),
        ]

        for start, end in arrow_positions:
            arrow = Arrow(start=start, end=end, color=WHITE, stroke_width=3, buff=0.1)
            arrows.add(arrow)

        self.play(Write(structure_title))
        self.play(Create(src_box), Write(src_label))
        self.play(Create(utils_box), Write(utils_label))
        self.play(Create(tests_box), Write(tests_label))
        self.play(Create(generate_llms_box), Write(generate_llms_label))
        self.play(Create(count_lines_box), Write(count_lines_label))
        self.play(Create(count_chars_box), Write(count_chars_label))
        self.play(Create(generate_toc_box), Write(generate_toc_label))
        self.play(Create(arrows))

        self.wait(4)
        self.play(FadeOut(structure_title), FadeOut(src_box), FadeOut(src_label),
                 FadeOut(utils_box), FadeOut(utils_label), FadeOut(tests_box), FadeOut(tests_label),
                 FadeOut(generate_llms_box), FadeOut(generate_llms_label),
                 FadeOut(count_lines_box), FadeOut(count_lines_label),
                 FadeOut(count_chars_box), FadeOut(count_chars_label),
                 FadeOut(generate_toc_box), FadeOut(generate_toc_label),
                 FadeOut(arrows))

        # Workflow animation
        workflow_title = Text("How It Works", font_size=40, color=PURPLE)

        # Create workflow steps
        step1 = VGroup(
            Text("1. Input Directory", font_size=28, color=BLUE),
            Text("User provides root directory path", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2)

        step2 = VGroup(
            Text("2. File Discovery", font_size=28, color=GREEN),
            Text("Scan for .md and code files", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2)

        step3 = VGroup(
            Text("3. Content Processing", font_size=28, color=ORANGE),
            Text("Extract titles, summaries, and code", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2)

        step4 = VGroup(
            Text("4. Generate Output", font_size=28, color=RED),
            Text("Create llms-full.txt with all content", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2)

        # Arrange steps in a circle
        workflow_title.move_to(UP*3)

        step1.move_to(UP*1.5 + LEFT*3)
        step2.move_to(UP*1.5 + RIGHT*3)
        step3.move_to(DOWN*1.5 + LEFT*3)
        step4.move_to(DOWN*1.5 + RIGHT*3)

        # Create arrows between steps
        workflow_arrows = VGroup(
            Arrow(step1.get_right(), step2.get_left(), color=YELLOW, buff=0.3),
            Arrow(step2.get_bottom(), step3.get_top(), color=YELLOW, buff=0.3),
            Arrow(step3.get_right(), step4.get_left(), color=YELLOW, buff=0.3),
            CurvedArrow(step4.get_left(), step1.get_bottom(), color=GREEN, angle=PI/2)
        )

        self.play(Write(workflow_title))
        self.play(Write(step1))
        self.play(Write(step2))
        self.play(Create(workflow_arrows[0]))
        self.play(Write(step3))
        self.play(Create(workflow_arrows[1]))
        self.play(Write(step4))
        self.play(Create(workflow_arrows[2]))
        self.play(Create(workflow_arrows[3]))

        self.wait(4)
        self.play(FadeOut(workflow_title), FadeOut(step1), FadeOut(step2),
                 FadeOut(step3), FadeOut(step4), FadeOut(workflow_arrows))

        # Key features
        features_title = Text("Key Features", font_size=40, color=BLUE)

        features = VGroup(
            Text("• Comprehensive Documentation Aggregation", font_size=24, color=TEAL),
            Text("• AI-Friendly Markdown Format", font_size=24, color=GREEN),
            Text("• Code and Text File Processing", font_size=24, color=ORANGE),
            Text("• Table of Contents Generation", font_size=24, color=PURPLE),
            Text("• Line and Character Counting", font_size=24, color=RED),
            Text("• Robust Error Handling", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        features_title.move_to(UP*3)
        features.move_to(ORIGIN)

        self.play(Write(features_title))
        for feature in features:
            self.play(FadeIn(feature))
        self.wait(3)

        # Final summary
        summary = VGroup(
            Text("LLMs-Full.txt Generator", font_size=36, color=YELLOW),
            Text("Bridging the gap between", font_size=24, color=WHITE),
            Text("human documentation and AI understanding", font_size=24, color=WHITE),
            Text("MIT-0 License", font_size=20, color=TEAL)
        ).arrange(DOWN, buff=0.3)

        self.play(FadeOut(features_title), FadeOut(features))
        self.play(Write(summary))
        self.wait(3)

        # Fade out
        self.play(FadeOut(summary))