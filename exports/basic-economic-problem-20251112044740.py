from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Configure scene for 1920x1080 aspect ratio and white background
        self.camera.background_color = WHITE
        self.camera.frame_width = 16  # Corresponds to 16:9 aspect ratio
        self.camera.frame_height = 9   # Corresponds to 16:9 aspect ratio

        # --- Phase 1: Title Introduction ---
        title = MarkupText(
            "<span foreground='black'>The Basic Economic Problem</span>",
            font_size=60
        )
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP).scale(0.7))

        # --- Phase 2: Core Concepts - Scarcity and Unlimited Wants ---
        scarcity_text = MarkupText(
            "<span foreground='#FF6347'>Scarcity</span>", # Tomato red
            font_size=48
        )
        wants_text = MarkupText(
            "<span foreground='#1E90FF'>Unlimited Wants</span>", # Dodger blue
            font_size=48
        )

        scarcity_text.next_to(title, DOWN, buff=1.5).shift(LEFT * 4)
        wants_text.next_to(title, DOWN, buff=1.5).shift(RIGHT * 4)

        self.play(FadeIn(scarcity_text, shift=LEFT), FadeIn(wants_text, shift=RIGHT))
        self.wait(1)

        # --- Phase 3: Visualizing Scarcity (Limited Resources) ---
        resources_box = Rectangle(
            width=3, height=2, color=GRAY, fill_opacity=0.2, stroke_width=2
        ).next_to(scarcity_text, DOWN, buff=0.8)
        resources_label = MarkupText(
            "<span foreground='black'>Resources</span>", font_size=30
        ).move_to(resources_box.get_top() + DOWN * 0.3)

        # Represent limited resources with a few dots inside the box
        resource_items = VGroup()
        for i in range(3):
            for j in range(2):
                dot = Dot(radius=0.15, color=GRAY).move_to(
                    resources_box.get_center() + LEFT * (0.8 - i * 0.8) + UP * (0.4 - j * 0.8)
                )
                resource_items.add(dot)

        limited_label = MarkupText(
            "<span foreground='#FF6347'>Limited</span>", font_size=36
        ).next_to(resources_box, DOWN, buff=0.5)

        self.play(
            Create(resources_box),
            FadeIn(resources_label),
            LaggedStart(*[FadeIn(item) for item in resource_items], lag_ratio=0.1),
            FadeIn(limited_label, shift=DOWN)
        )
        self.wait(1)

        # --- Phase 4: Visualizing Unlimited Wants ---
        wants_bubble = Circle(
            radius=2.5, color=BLUE_A, fill_opacity=0.1, stroke_width=2
        ).next_to(wants_text, DOWN, buff=0.8)
        wants_label = MarkupText(
            "<span foreground='black'>Wants</span>", font_size=30
        ).move_to(wants_bubble.get_top() + DOWN * 0.3)

        # Represent unlimited wants with many overflowing text items
        want_items = VGroup()
        want_texts = ["Food", "Shelter", "Clothes", "Fun", "Education", "Health", "Travel", "Luxury", "More!"]
        for i, text in enumerate(want_texts):
            want_mobject = MarkupText(
                f"<span foreground='#1E90FF'>{text}</span>", font_size=24
            ).move_to(wants_bubble.get_center() + complex_to_R3(2 * np.exp(1j * (i * PI / 4 + PI/8))))
            want_items.add(want_mobject)

        unlimited_label = MarkupText(
            "<span foreground='#1E90FF'>Unlimited</span>", font_size=36
        ).next_to(wants_bubble, DOWN, buff=0.5)

        self.play(
            Create(wants_bubble),
            FadeIn(wants_label),
            LaggedStart(*[FadeIn(item) for item in want_items], lag_ratio=0.1),
            FadeIn(unlimited_label, shift=DOWN)
        )
        self.wait(1)

        # --- Phase 5: The Conflict (Scarcity vs. Wants) ---
        # Fade out detailed visualizations and bring core concepts closer
        self.play(
            scarcity_text.animate.shift(RIGHT*1.5),
            wants_text.animate.shift(LEFT*1.5),
            FadeOut(resources_box, resources_label, resource_items, limited_label),
            FadeOut(wants_bubble, wants_label, want_items, unlimited_label)
        )
        self.wait(0.5)

        # Create arrow and label to show the conflict
        conflict_arrow = Arrow(
            start=scarcity_text.get_right(),
            end=wants_text.get_left(),
            color=RED,
            stroke_width=5
        )
        conflict_label = MarkupText(
            "<span foreground='black'>Leads to...</span>", font_size=36
        ).next_to(conflict_arrow, UP, buff=0.3)

        imbalance_text = MarkupText(
            "<span foreground='#8B0000'>Imbalance / Conflict</span>", # Dark red
            font_size=50
        ).next_to(conflict_arrow, DOWN, buff=0.5)

        self.play(
            Create(conflict_arrow),
            FadeIn(conflict_label)
        )
        self.play(FadeIn(imbalance_text, shift=UP))
        self.wait(1.5)

        # --- Phase 6: The Solution - Choice ---
        requires_arrow = Arrow(
            start=imbalance_text.get_bottom(),
            end=imbalance_text.get_bottom() + DOWN * 2,
            color=PURPLE,
            stroke_width=4
        )
        requires_label = MarkupText(
            "<span foreground='black'>Requires...</span>", font_size=36
        ).next_to(requires_arrow, LEFT, buff=0.3)

        choice_text = MarkupText(
            "<span foreground='#8A2BE2'>Choice</span>", # Blue Violet
            font_size=60
        ).next_to(requires_arrow, DOWN, buff=0.5)

        self.play(
            Create(requires_arrow),
            FadeIn(requires_label)
        )
        self.play(FadeIn(choice_text, shift=DOWN))
        self.wait(1)

        # --- Phase 7: The Three Basic Economic Questions ---
        questions_group = VGroup()
        q1 = MarkupText(
            "<span foreground='black'>1. What to produce?</span>", font_size=36
        )
        q2 = MarkupText(
            "<span foreground='black'>2. How to produce?</span>", font_size=36
        )
        q3 = MarkupText(
            "<span foreground='black'>3. For whom to produce?</span>", font_size=36
        )

        questions_group.add(q1, q2, q3).arrange(DOWN, buff=0.7)
        questions_group.next_to(choice_text, DOWN, buff=1.0)

        self.play(
            FadeIn(q1, shift=UP),
            run_time=0.8
        )
        self.play(
            FadeIn(q2, shift=UP),
            run_time=0.8
        )
        self.play(
            FadeIn(q3, shift=UP),
            run_time=0.8
        )
        self.wait(2)

        # --- Final Fade Out ---
        self.play(
            FadeOut(title, shift=UP),
            FadeOut(scarcity_text, shift=LEFT),
            FadeOut(wants_text, shift=RIGHT),
            FadeOut(conflict_arrow, conflict_label, imbalance_text),
            FadeOut(requires_arrow, requires_label, choice_text),
            FadeOut(questions_group, shift=DOWN),
            run_time=2
        )
        self.wait(1)