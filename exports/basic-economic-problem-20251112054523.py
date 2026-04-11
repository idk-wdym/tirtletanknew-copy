from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Configure resolution and FPS
        self.camera.background_color = BLACK
        self.camera.frame_width = 16
        self.camera.frame_height = 9
        self.camera.pixel_width = 1920
        self.camera.pixel_height = 1080
        self.renderer.frame_rate = 30

        # --- Introduction: The Basic Economic Problem ---
        title = MathTex(r"\textbf{The Basic Economic Problem}", font_size=72, color=BLUE)
        self.play(Write(title))
        self.wait(1)

        intro_text = MathTex(
            r"\text{Economics deals with how societies allocate scarce resources}",
            r"\\",
            r"\text{to satisfy unlimited wants and needs.}",
            font_size=48,
            color=WHITE
        ).next_to(title, DOWN, buff=1)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(intro_text))
        self.wait(0.5)

        # --- Concept 1: Scarcity ---
        scarcity_title = MathTex(r"\textbf{1. Scarcity}", font_size=60, color=YELLOW).to_edge(UP + LEFT)
        self.play(Write(scarcity_title))
        self.wait(0.5)

        scarcity_def = MathTex(
            r"\text{The fundamental problem of economics:}",
            r"\\",
            r"\text{Unlimited human wants and needs}",
            r"\\",
            r"\text{exceed the limited resources available to satisfy them.}",
            font_size=40,
            color=WHITE
        ).next_to(scarcity_title, DOWN, buff=0.5).align_to(scarcity_title, LEFT)
        self.play(Write(scarcity_def))
        self.wait(2)

        # Visualizing Scarcity with text-based representations
        wants_list = VGroup(
            MathTex(r"\text{Food}", color=WHITE),
            MathTex(r"\text{Shelter}", color=WHITE),
            MathTex(r"\text{Education}", color=WHITE),
            MathTex(r"\text{Entertainment}", color=WHITE),
            MathTex(r"\text{Healthcare}", color=WHITE),
            MathTex(r"\text{Luxury Goods}", color=WHITE)
        ).arrange_in_grid(rows=3, cols=2, buff=0.5).set_height(4).shift(LEFT * 4)

        resources_list = VGroup(
            MathTex(r"\text{Land}", color=WHITE),
            MathTex(r"\text{Labor}", color=WHITE),
            MathTex(r"\text{Capital}", color=WHITE),
            MathTex(r"\text{Entrepreneurship}", color=WHITE)
        ).arrange(DOWN, buff=0.7).set_height(3).shift(RIGHT * 4)

        unlimited_wants_label = MathTex(r"\text{Unlimited Wants}", font_size=45, color=GREEN).next_to(wants_list, UP, buff=0.5)
        limited_resources_label = MathTex(r"\text{Limited Resources}", font_size=45, color=RED).next_to(resources_list, UP, buff=0.5)

        self.play(
            FadeIn(unlimited_wants_label, shift=UP),
            FadeIn(limited_resources_label, shift=UP),
            LaggedStart(*[FadeIn(want, shift=LEFT) for want in wants_list], lag_ratio=0.1),
            LaggedStart(*[FadeIn(res, shift=RIGHT) for res in resources_list], lag_ratio=0.1)
        )
        self.wait(2)

        arrow_left = Arrow(start=unlimited_wants_label.get_right(), end=limited_resources_label.get_left(), color=ORANGE, buff=0.5)
        arrow_right = Arrow(start=limited_resources_label.get_left(), end=unlimited_wants_label.get_right(), color=ORANGE, buff=0.5)
        conflict_text = MathTex(r"\textbf{Conflict!}", font_size=50, color=ORANGE).next_to(arrow_left, UP, buff=0.5)

        self.play(GrowArrow(arrow_left), GrowArrow(arrow_right), Write(conflict_text))
        self.wait(2)

        self.play(
            FadeOut(scarcity_title),
            FadeOut(scarcity_def),
            FadeOut(unlimited_wants_label),
            FadeOut(limited_resources_label),
            FadeOut(wants_list),
            FadeOut(resources_list),
            FadeOut(arrow_left),
            FadeOut(arrow_right),
            FadeOut(conflict_text)
        )
        self.wait(0.5)

        # --- Concept 2: Choice ---
        choice_title = MathTex(r"\textbf{2. Choice}", font_size=60, color=YELLOW).to_edge(UP + LEFT)
        self.play(Write(choice_title))
        self.wait(0.5)

        choice_def = MathTex(
            r"\text{Because resources are scarce, societies and individuals}",
            r"\\",
            r"\text{must make choices about how to allocate them.}",
            font_size=40,
            color=WHITE
        ).next_to(choice_title, DOWN, buff=0.5).align_to(choice_title, LEFT)
        self.play(Write(choice_def))
        self.wait(2)

        # Visualizing Choice
        option_a_text = MathTex(r"\text{Option A: Invest in Education}", font_size=45, color=GREEN).shift(LEFT * 3)
        option_b_text = MathTex(r"\text{Option B: Invest in Healthcare}", font_size=45, color=RED).shift(RIGHT * 3)

        decision_point = Dot(point=ORIGIN, radius=0.2, color=BLUE)
        decision_label = MathTex(r"\textbf{Decision Point}", font_size=40, color=BLUE).next_to(decision_point, UP)

        arrow_a = Arrow(start=decision_point.get_top(), end=option_a_text.get_bottom(), color=WHITE)
        arrow_b = Arrow(start=decision_point.get_top(), end=option_b_text.get_bottom(), color=WHITE)

        self.play(
            GrowFromCenter(decision_point),
            Write(decision_label)
        )
        self.wait(0.5)
        self.play(
            GrowArrow(arrow_a), Write(option_a_text),
            GrowArrow(arrow_b), Write(option_b_text)
        )
        self.wait(2)

        # Simulate making a choice
        chosen_option_box = SurroundingRectangle(option_a_text, color=GREEN, buff=0.2)
        self.play(Create(chosen_option_box))
        self.wait(1)
        self.play(FadeOut(option_b_text), FadeOut(arrow_b))
        self.wait(1)

        self.play(
            FadeOut(choice_title),
            FadeOut(choice_def),
            FadeOut(decision_point),
            FadeOut(decision_label),
            FadeOut(arrow_a),
            FadeOut(option_a_text),
            FadeOut(chosen_option_box)
        )
        self.wait(0.5)

        # --- Concept 3: Opportunity Cost ---
        opp_cost_title = MathTex(r"\textbf{3. Opportunity Cost}", font_size=60, color=YELLOW).to_edge(UP + LEFT)
        self.play(Write(opp_cost_title))
        self.wait(0.5)

        opp_cost_def = MathTex(
            r"\text{The value of the next best alternative}",
            r"\\",
            r"\text{that was not chosen when a decision was made.}",
            font_size=40,
            color=WHITE
        ).next_to(opp_cost_title, DOWN, buff=0.5).align_to(opp_cost_title, LEFT)
        self.play(Write(opp_cost_def))
        self.wait(2)

        # Example 1: Individual Choice - Student's Dilemma
        example1_label = MathTex(r"\textbf{Example 1: Student's Dilemma}", font_size=45, color=ORANGE).next_to(opp_cost_def, DOWN, buff=1).align_to(opp_cost_def, LEFT)
        self.play(Write(example1_label))
        self.wait(0.5)

        scenario_text = MathTex(
            r"\text{A student has \$100. Options:}",
            r"\\",
            r"\text{1. Buy a new textbook for \$100}",
            r"\\",
            r"\text{2. Go to a concert for \$100}",
            font_size=36,
            color=WHITE
        ).next_to(example1_label, DOWN, buff=0.5).align_to(example1_label, LEFT)
        self.play(Write(scenario_text))
        self.wait(2)

        textbook_option = MathTex(r"\text{Buy Textbook}", font_size=40, color=BLUE).shift(LEFT * 3 + DOWN * 2)
        concert_option = MathTex(r"\text{Go to Concert}", font_size=40, color=RED).shift(RIGHT * 3 + DOWN * 2)

        self.play(FadeIn(textbook_option, shift=UP), FadeIn(concert_option, shift=UP))
        self.wait(1)

        # Student chooses textbook
        chosen_textbook_box = SurroundingRectangle(textbook_option, color=BLUE, buff=0.2)
        self.play(Create(chosen_textbook_box))
        self.wait(1)

        foregone_concert_text = MathTex(r"\text{Foregone}", font_size=30, color=GRAY).next_to(concert_option, DOWN, buff=0.2)
        self.play(FadeOut(concert_option, target_mode="fade_and_shift_down"), Write(foregone_concert_text))
        self.wait(1)

        opp_cost_result = MathTex(
            r"\text{Opportunity Cost: The Concert}",
            r"\\",
            r"\text{(the enjoyment and experience of the concert)}",
            font_size=38,
            color=GREEN
        ).next_to(chosen_textbook_box, DOWN, buff=0.7)
        self.play(Write(opp_cost_result))
        self.wait(3)

        self.play(
            FadeOut(opp_cost_title),
            FadeOut(opp_cost_def),
            FadeOut(example1_label),
            FadeOut(scenario_text),
            FadeOut(textbook_option),
            FadeOut(chosen_textbook_box),
            FadeOut(foregone_concert_text),
            FadeOut(opp_cost_result)
        )
        self.wait(0.5)

        # Example 2: Production Possibilities Frontier (PPF)
        example2_label = MathTex(r"\textbf{Example 2: Production Possibilities Frontier (PPF)}", font_size=45, color=ORANGE).to_edge(UP + LEFT)
        self.play(Write(example2_label))
        self.wait(0.5)

        ppf_intro = MathTex(
            r"\text{The PPF illustrates the trade-offs facing an economy}",
            r"\\",
            r"\text{that produces two goods with fixed resources and technology.}",
            font_size=38,
            color=WHITE
        ).next_to(example2_label, DOWN, buff=0.5).align_to(example2_label, LEFT)
        self.play(Write(ppf_intro))
        self.wait(2)

        # Clear screen for graph
        self.play(FadeOut(example2_label), FadeOut(ppf_intro))
        self.wait(0.5)

        # Create Axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=7,
            y_length=7,
            axis_config={"color": GRAY, "include_numbers": True},
            tips=False
        ).to_edge(DOWN + LEFT, buff=1)

        x_label = axes.get_x_axis_label(MathTex(r"\text{Consumer Goods}", font_size=30, color=WHITE)).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = axes.get_y_axis_label(MathTex(r"\text{Capital Goods}", font_size=30, color=WHITE), edge=LEFT, direction=UP).next_to(axes.y_axis, LEFT, buff=0.2)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        # Define the PPF curve (concave to the origin, showing increasing opportunity cost)
        def ppf_func(x):
            return -0.15 * x**2 + 10

        ppf_curve = axes.plot(ppf_func, x_range=[0, 8], color=BLUE)
        ppf_label = MathTex(r"\text{PPF}", font_size=35, color=BLUE).next_to(ppf_curve, UP + RIGHT, buff=0.1)

        self.play(Create(ppf_curve), Write(ppf_label))
        self.wait(1)

        # Points on the PPF
        point_a_coords = [2, ppf_func(2)]
        point_b_coords = [6, ppf_func(6)]
        point_c_coords = [3, 3] # Inefficient
        point_d_coords = [7, 7] # Unattainable

        point_a = Dot(axes.coords_to_point(*point_a_coords), color=GREEN)
        label_a = MathTex(r"A", font_size=30, color=GREEN).next_to(point_a, UP + LEFT)
        point_a_text = MathTex(r"\text{Efficient}", font_size=28, color=GREEN).next_to(label_a, UP, buff=0.1)

        point_b = Dot(axes.coords_to_point(*point_b_coords), color=GREEN)
        label_b = MathTex(r"B", font_size=30, color=GREEN).next_to(point_b, UP + RIGHT)
        point_b_text = MathTex(r"\text{Efficient}", font_size=28, color=GREEN).next_to(label_b, UP, buff=0.1)

        point_c = Dot(axes.coords_to_point(*point_c_coords), color=YELLOW)
        label_c = MathTex(r"C", font_size=30, color=YELLOW).next_to(point_c, DOWN + LEFT)
        point_c_text = MathTex(r"\text{Inefficient}", font_size=28, color=YELLOW).next_to(label_c, DOWN, buff=0.1)

        point_d = Dot(axes.coords_to_point(*point_d_coords), color=RED)
        label_d = MathTex(r"D", font_size=30, color=RED).next_to(point_d, UP + RIGHT)
        point_d_text = MathTex(r"\text{Unattainable}", font_size=28, color=RED).next_to(label_d, UP, buff=0.1)

        self.play(
            FadeIn(point_a, shift=UP), Write(label_a), Write(point_a_text),
            FadeIn(point_b, shift=UP), Write(label_b), Write(point_b_text)
        )
        self.wait(1)
        self.play(
            FadeIn(point_c, shift=UP), Write(label_c), Write(point_c_text)
        )
        self.wait(1)
        self.play(
            FadeIn(point_d, shift=UP), Write(label_d), Write(point_d_text)
        )
        self.wait(2)

        # Explain opportunity cost on PPF
        explanation_text_ppf = MathTex(
            r"\text{Moving from A to B: To produce more Consumer Goods,}",
            r"\\",
            r"\text{we must give up some Capital Goods. This is the Opportunity Cost.}",
            font_size=38,
            color=WHITE
        ).to_edge(UP + RIGHT, buff=0.5)
        self.play(Write(explanation_text_ppf))
        self.wait(1)

        # Highlight movement from A to B
        path_ab = Line(point_a.get_center(), point_b.get_center(), color=PURPLE, stroke_width=5)
        arrow_ab = Arrow(start=point_a.get_center(), end=point_b.get_center(), color=PURPLE, buff=0.1)

        self.play(
            Indicate(point_a),
            Indicate(point_b),
            Create(path_ab),
            GrowArrow(arrow_ab)
        )
        self.wait(2)

        # Show the trade-off with dashed lines
        line_a_x = axes.get_vertical_line(point_a, color=GRAY_A, dash_array=[0.1, 0.1])
        line_a_y = axes.get_horizontal_line(point_a, color=GRAY_A, dash_array=[0.1, 0.1])
        line_b_x = axes.get_vertical_line(point_b, color=GRAY_A, dash_array=[0.1, 0.1])
        line_b_y = axes.get_horizontal_line(point_b, color=GRAY_A, dash_array=[0.1, 0.1])

        self.play(Create(line_a_x), Create(line_a_y))
        self.play(Create(line_b_x), Create(line_b_y))
        self.wait(1)

        # Indicate the change in Y (capital goods given up)
        capital_loss_line = Line(axes.coords_to_point(0, point_a_coords[1]), axes.coords_to_point(0, point_b_coords[1]), color=RED, stroke_width=4)
        capital_loss_label = MathTex(r"\Delta \text{Capital Goods (Cost)}", font_size=30, color=RED).next_to(capital_loss_line, LEFT, buff=0.2)

        # Indicate the change in X (consumer goods gained)
        consumer_gain_line = Line(axes.coords_to_point(point_a_coords[0], 0), axes.coords_to_point(point_b_coords[0], 0), color=GREEN, stroke_width=4)
        consumer_gain_label = MathTex(r"\Delta \text{Consumer Goods (Gain)}", font_size=30, color=GREEN).next_to(consumer_gain_line, DOWN, buff=0.2)

        self.play(
            Create(capital_loss_line), Write(capital_loss_label),
            Create(consumer_gain_line), Write(consumer_gain_label)
        )
        self.wait(3)

        # Clear graph and its components
        self.play(
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(ppf_curve),
            FadeOut(ppf_label),
            FadeOut(point_a), FadeOut(label_a), FadeOut(point_a_text),
            FadeOut(point_b), FadeOut(label_b), FadeOut(point_b_text),
            FadeOut(point_c), FadeOut(label_c), FadeOut(point_c_text),
            FadeOut(point_d), FadeOut(label_d), FadeOut(point_d_text),
            FadeOut(explanation_text_ppf),
            FadeOut(path_ab), FadeOut(arrow_ab),
            FadeOut(line_a_x), FadeOut(line_a_y),
            FadeOut(line_b_x), FadeOut(line_b_y),
            FadeOut(capital_loss_line), FadeOut(capital_loss_label),
            FadeOut(consumer_gain_line), FadeOut(consumer_gain_label)
        )
        self.wait(1)

        # --- Conclusion ---
        conclusion_title = MathTex(r"\textbf{Summary}", font_size=60, color=BLUE).to_edge(UP)
        self.play(Write(conclusion_title))
        self.wait(0.5)

        summary_points = VGroup(
            MathTex(r"\text{1. Scarcity: Unlimited wants, limited resources.}", font_size=45, color=WHITE),
            MathTex(r"\text{2. Choice: Decisions must be made due to scarcity.}", font_size=45, color=WHITE),
            MathTex(r"\text{3. Opportunity Cost: The value of the next best alternative foregone.}", font_size=45, color=WHITE)
        ).arrange(DOWN, buff=0.8, aligned_edge=LEFT).next_to(conclusion_title, DOWN, buff=1)

        self.play(LaggedStart(*[Write(point) for point in summary_points], lag_ratio=0.7))
        self.wait(3)

        final_message = MathTex(
            r"\text{Understanding these concepts is crucial}",
            r"\\",
            r"\text{for analyzing economic behavior and policy.}",
            font_size=48,
            color=GREEN
        ).next_to(summary_points, DOWN, buff=1.5)
        self.play(Write(final_message))
        self.wait(3)

        self.play(FadeOut(conclusion_title), FadeOut(summary_points), FadeOut(final_message))
        self.wait(1)