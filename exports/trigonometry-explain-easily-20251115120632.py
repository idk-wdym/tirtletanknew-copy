from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Configure scene resolution and background
        config.frame_width = 16
        config.frame_height = 9
        config.frame_rate = 30
        config.background_color = WHITE

        # Define custom colors for better visual separation and contrast
        COLOR_TITLE = BLACK
        COLOR_DEFINITION = BLACK
        COLOR_HIGHLIGHT = BLUE_C
        COLOR_TRIANGLE = BLUE_A
        COLOR_RIGHT_ANGLE = GRAY_A
        COLOR_ANGLE = RED_C
        COLOR_HYPOTENUSE = ORANGE
        COLOR_OPPOSITE = GREEN_C
        COLOR_ADJACENT = PURPLE_C
        COLOR_MNEMONIC = TEAL_C
        COLOR_EXAMPLE_TITLE = BLACK
        COLOR_STEP = BLACK
        COLOR_CALCULATION = BLACK
        COLOR_RESULT = RED_E

        # --- Scene 1: Introduction to Trigonometry ---
        title = MathTex(r"\text{Understanding Trigonometry}", color=COLOR_TITLE).scale(1.5).to_edge(UP, buff=0.7)
        definition = MathTex(
            r"\text{Trigonometry is the study of relationships}",
            r"\text{between angles and sides of triangles.}",
            color=COLOR_DEFINITION
        ).scale(0.9).next_to(title, DOWN, buff=0.8)
        focus = MathTex(
            r"\text{It primarily deals with right-angled triangles.}",
            color=COLOR_DEFINITION
        ).scale(0.9).next_to(definition, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Write(definition[0]), Write(definition[1]))
        self.play(Write(focus))
        self.wait(1)

        # Draw a generic right-angled triangle
        p1 = LEFT * 3 + DOWN * 2
        p2 = RIGHT * 1 + DOWN * 2
        p3 = LEFT * 3 + UP * 1.5
        triangle = Polygon(p1, p2, p3, color=COLOR_TRIANGLE, fill_opacity=0.4, stroke_width=4)
        right_angle_square = Square(side_length=0.4, color=COLOR_RIGHT_ANGLE, fill_opacity=0.8).move_to(p1 + RIGHT * 0.2 + UP * 0.2)

        self.play(Create(triangle), Create(right_angle_square))
        self.wait(2)

        self.play(FadeOut(VGroup(title, definition, focus, triangle, right_angle_square)))
        self.wait(0.5)

        # --- Scene 2: Naming the Sides ---
        self.clear()

        # Redraw the triangle for side labeling
        p1 = LEFT * 3 + DOWN * 2
        p2 = RIGHT * 1 + DOWN * 2
        p3 = LEFT * 3 + UP * 1.5
        triangle = Polygon(p1, p2, p3, color=COLOR_TRIANGLE, fill_opacity=0.4, stroke_width=4).shift(LEFT*2)
        right_angle_square = Square(side_length=0.4, color=COLOR_RIGHT_ANGLE, fill_opacity=0.8).move_to(p1 + RIGHT * 0.2 + UP * 0.2)

        self.play(Create(triangle), Create(right_angle_square))

        # Define the angle of interest (theta)
        angle_vertex = p1
        line_adjacent = Line(p1, p2)
        line_opposite = Line(p1, p3)
        angle_theta = Angle(line_adjacent, line_opposite, radius=0.7, color=COLOR_ANGLE, other_angle=False)
        theta_label = MathTex(r"\theta", color=COLOR_ANGLE).next_to(angle_theta, DR, buff=0.1)

        self.play(Create(angle_theta), Write(theta_label))
        self.wait(1)

        # Label the sides relative to theta
        hypotenuse_line = Line(p2, p3)
        opposite_line = Line(p1, p3)
        adjacent_line = Line(p1, p2)

        hypotenuse_label = MathTex(r"\text{Hypotenuse}", color=COLOR_HYPOTENUSE).next_to(hypotenuse_line, UP + RIGHT, buff=0.2).shift(LEFT*0.5)
        opposite_label = MathTex(r"\text{Opposite}", color=COLOR_OPPOSITE).next_to(opposite_line, LEFT, buff=0.2)
        adjacent_label = MathTex(r"\text{Adjacent}", color=COLOR_ADJACENT).next_to(adjacent_line, DOWN, buff=0.2)

        self.play(Write(hypotenuse_label), FadeIn(hypotenuse_line.set_color(COLOR_HYPOTENUSE)))
        self.wait(0.5)
        self.play(Write(opposite_label), FadeIn(opposite_line.set_color(COLOR_OPPOSITE)))
        self.wait(0.5)
        self.play(Write(adjacent_label), FadeIn(adjacent_line.set_color(COLOR_ADJACENT)))
        self.wait(2)

        # Introduce SOH CAH TOA mnemonic
        mnemonic_title = MathTex(r"\text{Remember:}", color=COLOR_DEFINITION).scale(1.1).to_edge(UP, buff=0.7).shift(RIGHT*3)
        mnemonic = MathTex(
            r"\text{SOH CAH TOA}",
            color=COLOR_MNEMONIC
        ).scale(1.5).next_to(mnemonic_title, DOWN, buff=0.5)

        self.play(Write(mnemonic_title))
        self.play(Write(mnemonic))
        self.wait(2)

        all_elements_scene2 = VGroup(
            triangle, right_angle_square, angle_theta, theta_label,
            hypotenuse_label, opposite_label, adjacent_label,
            hypotenuse_line, opposite_line, adjacent_line,
            mnemonic_title, mnemonic
        )
        self.play(FadeOut(all_elements_scene2))
        self.wait(0.5)

        # --- Scene 3: The Trigonometric Ratios ---
        self.clear()

        # Redraw a smaller triangle to the left
        p1_small = LEFT * 6 + DOWN * 1.5
        p2_small = LEFT * 4 + DOWN * 1.5
        p3_small = LEFT * 6 + UP * 0.5
        triangle_small = Polygon(p1_small, p2_small, p3_small, color=COLOR_TRIANGLE, fill_opacity=0.4, stroke_width=3)
        right_angle_square_small = Square(side_length=0.3, color=COLOR_RIGHT_ANGLE, fill_opacity=0.8).move_to(p1_small + RIGHT * 0.15 + UP * 0.15)
        angle_theta_small = Angle(Line(p1_small, p2_small), Line(p1_small, p3_small), radius=0.5, color=COLOR_ANGLE, other_angle=False)
        theta_label_small = MathTex(r"\theta", color=COLOR_ANGLE).next_to(angle_theta_small, DR, buff=0.05)

        hypotenuse_label_small = MathTex(r"\text{Hyp.}", color=COLOR_HYPOTENUSE).next_to(Line(p2_small, p3_small), UP + RIGHT, buff=0.1).shift(LEFT*0.2)
        opposite_label_small = MathTex(r"\text{Opp.}", color=COLOR_OPPOSITE).next_to(Line(p1_small, p3_small), LEFT, buff=0.1)
        adjacent_label_small = MathTex(r"\text{Adj.}", color=COLOR_ADJACENT).next_to(Line(p1_small, p2_small), DOWN, buff=0.1)

        triangle_group = VGroup(
            triangle_small, right_angle_square_small, angle_theta_small, theta_label_small,
            hypotenuse_label_small, opposite_label_small, adjacent_label_small
        )
        self.play(Create(triangle_group))
        self.wait(1)

        # Display the trigonometric ratios
        ratio_title = MathTex(r"\text{The Trigonometric Ratios}", color=COLOR_TITLE).scale(1.2).to_edge(UP, buff=0.7)
        self.play(Write(ratio_title))

        sin_eq = MathTex(
            r"\text{SOH: }", r"\sin(\theta) = \frac{\text{Opposite}}{\text{Hypotenuse}}",
            color=COLOR_OPPOSITE
        ).scale(1.1).next_to(ratio_title, DOWN, buff=0.8).align_to(triangle_group, LEFT).shift(RIGHT*4)

        cos_eq = MathTex(
            r"\text{CAH: }", r"\cos(\theta) = \frac{\text{Adjacent}}{\text{Hypotenuse}}",
            color=COLOR_ADJACENT
        ).scale(1.1).next_to(sin_eq, DOWN, buff=0.5).align_to(sin_eq, LEFT)

        tan_eq = MathTex(
            r"\text{TOA: }", r"\tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}",
            color=COLOR_HYPOTENUSE # Using Hypotenuse color for tan, as it's the remaining one
        ).scale(1.1).next_to(cos_eq, DOWN, buff=0.5).align_to(sin_eq, LEFT)

        self.play(Write(sin_eq[0]), Write(sin_eq[1]))
        self.wait(1)
        self.play(Write(cos_eq[0]), Write(cos_eq[1]))
        self.wait(1)
        self.play(Write(tan_eq[0]), Write(tan_eq[1]))
        self.wait(2)

        all_elements_scene3 = VGroup(
            triangle_group, ratio_title, sin_eq, cos_eq, tan_eq
        )
        self.play(FadeOut(all_elements_scene3))
        self.wait(0.5)

        # --- Scene 4: Example 1 - Finding a Missing Side ---
        self.clear()

        example_title1 = MathTex(r"\text{Example 1: Finding a Missing Side}", color=COLOR_EXAMPLE_TITLE).scale(1.2).to_edge(UP, buff=0.7)
        self.play(Write(example_title1))
        self.wait(0.5)

        # Draw triangle for example 1
        p1_ex1 = LEFT * 5 + DOWN * 2
        p2_ex1 = LEFT * 1 + DOWN * 2
        p3_ex1 = LEFT * 5 + UP * 1.5
        triangle_ex1 = Polygon(p1_ex1, p2_ex1, p3_ex1, color=COLOR_TRIANGLE, fill_opacity=0.4, stroke_width=4)
        right_angle_square_ex1 = Square(side_length=0.4, color=COLOR_RIGHT_ANGLE, fill_opacity=0.8).move_to(p1_ex1 + RIGHT * 0.2 + UP * 0.2)

        angle_value_ex1 = MathTex(r"30^\circ", color=COLOR_ANGLE).move_to(p1_ex1 + RIGHT * 0.7 + UP * 0.4)
        angle_arc_ex1 = Angle(Line(p1_ex1, p2_ex1), Line(p1_ex1, p3_ex1), radius=0.7, color=COLOR_ANGLE, other_angle=False)

        hypotenuse_value_ex1 = MathTex(r"10", color=COLOR_HYPOTENUSE).next_to(Line(p2_ex1, p3_ex1), UP + RIGHT, buff=0.2).shift(LEFT*0.5)
        opposite_unknown_ex1 = MathTex(r"x", color=COLOR_OPPOSITE).next_to(Line(p1_ex1, p3_ex1), LEFT, buff=0.2)
        adjacent_label_ex1 = MathTex(r"\text{Adj.}", color=COLOR_ADJACENT).next_to(Line(p1_ex1, p2_ex1), DOWN, buff=0.2)

        self.play(Create(triangle_ex1), Create(right_angle_square_ex1))
        self.play(Create(angle_arc_ex1), Write(angle_value_ex1))
        self.play(Write(hypotenuse_value_ex1), Write(opposite_unknown_ex1), Write(adjacent_label_ex1))
        self.wait(1)

        # Steps for solving
        step1_ex1 = MathTex(r"\text{1. Identify knowns: Angle } 30^\circ \text{, Hypotenuse } 10 \text{.}", color=COLOR_STEP).scale(0.8).to_edge(RIGHT, buff=0.5).shift(UP*2.5)
        step2_ex1 = MathTex(r"\text{   Unknown: Opposite side } x \text{.}", color=COLOR_STEP).scale(0.8).next_to(step1_ex1, DOWN, buff=0.2).align_to(step1_ex1, LEFT)
        step3_ex1 = MathTex(r"\text{2. Choose ratio: Opposite and Hypotenuse } \Rightarrow \text{ SOH (Sine)}", color=COLOR_STEP).scale(0.8).next_to(step2_ex1, DOWN, buff=0.5).align_to(step1_ex1, LEFT)
        step4_ex1 = MathTex(r"\text{3. Set up equation and solve:}", color=COLOR_STEP).scale(0.8).next_to(step3_ex1, DOWN, buff=0.5).align_to(step1_ex1, LEFT)

        self.play(Write(step1_ex1))
        self.play(Write(step2_ex1))
        self.play(Write(step3_ex1))
        self.play(Write(step4_ex1))
        self.wait(1)

        calc1_ex1 = MathTex(r"\sin(\theta) = \frac{\text{Opposite}}{\text{Hypotenuse}}", color=COLOR_CALCULATION).scale(0.9).next_to(step4_ex1, DOWN, buff=0.3).align_to(step4_ex1, LEFT)
        calc2_ex1 = MathTex(r"\sin(30^\circ) = \frac{x}{10}", color=COLOR_CALCULATION).scale(0.9).next_to(calc1_ex1, DOWN, buff=0.2).align_to(calc1_ex1, LEFT)
        calc3_ex1 = MathTex(r"x = 10 \times \sin(30^\circ)", color=COLOR_CALCULATION).scale(0.9).next_to(calc2_ex1, DOWN, buff=0.2).align_to(calc1_ex1, LEFT)
        calc4_ex1 = MathTex(r"x = 10 \times 0.5", color=COLOR_CALCULATION).scale(0.9).next_to(calc3_ex1, DOWN, buff=0.2).align_to(calc1_ex1, LEFT)
        result_ex1 = MathTex(r"x = 5", color=COLOR_RESULT).scale(1.2).next_to(calc4_ex1, DOWN, buff=0.5).align_to(calc1_ex1, LEFT)

        self.play(Write(calc1_ex1))
        self.play(TransformMatchingTex(calc1_ex1.copy(), calc2_ex1))
        self.play(TransformMatchingTex(calc2_ex1.copy(), calc3_ex1))
        self.play(TransformMatchingTex(calc3_ex1.copy(), calc4_ex1))
        self.play(TransformMatchingTex(calc4_ex1.copy(), result_ex1))
        self.wait(2)

        all_elements_scene4 = VGroup(
            example_title1, triangle_ex1, right_angle_square_ex1, angle_value_ex1, angle_arc_ex1,
            hypotenuse_value_ex1, opposite_unknown_ex1, adjacent_label_ex1,
            step1_ex1, step2_ex1, step3_ex1, step4_ex1,
            calc1_ex1, calc2_ex1, calc3_ex1, calc4_ex1, result_ex1
        )
        self.play(FadeOut(all_elements_scene4))
        self.wait(0.5)

        # --- Scene 5: Example 2 - Finding a Missing Angle ---
        self.clear()

        example_title2 = MathTex(r"\text{Example 2: Finding a Missing Angle}", color=COLOR_EXAMPLE_TITLE).scale(1.2).to_edge(UP, buff=0.7)
        self.play(Write(example_title2))
        self.wait(0.5)

        # Draw triangle for example 2
        p1_ex2 = LEFT * 5 + DOWN * 2
        p2_ex2 = LEFT * 1 + DOWN * 2
        p3_ex2 = LEFT * 5 + UP * 1.5
        triangle_ex2 = Polygon(p1_ex2, p2_ex2, p3_ex2, color=COLOR_TRIANGLE, fill_opacity=0.4, stroke_width=4)
        right_angle_square_ex2 = Square(side_length=0.4, color=COLOR_RIGHT_ANGLE, fill_opacity=0.8).move_to(p1_ex2 + RIGHT * 0.2 + UP * 0.2)

        angle_unknown_ex2 = MathTex(r"\theta", color=COLOR_ANGLE).move_to(p1_ex2 + RIGHT * 0.7 + UP * 0.4)
        angle_arc_ex2 = Angle(Line(p1_ex2, p2_ex2), Line(p1_ex2, p3_ex2), radius=0.7, color=COLOR_ANGLE, other_angle=False)

        hypotenuse_value_ex2 = MathTex(r"10", color=COLOR_HYPOTENUSE).next_to(Line(p2_ex2, p3_ex2), UP + RIGHT, buff=0.2).shift(LEFT*0.5)
        opposite_label_ex2 = MathTex(r"\text{Opp.}", color=COLOR_OPPOSITE).next_to(Line(p1_ex2, p3_ex2), LEFT, buff=0.2)
        adjacent_value_ex2 = MathTex(r"8", color=COLOR_ADJACENT).next_to(Line(p1_ex2, p2_ex2), DOWN, buff=0.2)

        self.play(Create(triangle_ex2), Create(right_angle_square_ex2))
        self.play(Create(angle_arc_ex2), Write(angle_unknown_ex2))
        self.play(Write(hypotenuse_value_ex2), Write(opposite_label_ex2), Write(adjacent_value_ex2))
        self.wait(1)

        # Steps for solving
        step1_ex2 = MathTex(r"\text{1. Identify knowns: Adjacent } 8 \text{, Hypotenuse } 10 \text{.}", color=COLOR_STEP).scale(0.8).to_edge(RIGHT, buff=0.5).shift(UP*2.5)
        step2_ex2 = MathTex(r"\text{   Unknown: Angle } \theta \text{.}", color=COLOR_STEP).scale(0.8).next_to(step1_ex2, DOWN, buff=0.2).align_to(step1_ex2, LEFT)
        step3_ex2 = MathTex(r"\text{2. Choose ratio: Adjacent and Hypotenuse } \Rightarrow \text{ CAH (Cosine)}", color=COLOR_STEP).scale(0.8).next_to(step2_ex2, DOWN, buff=0.5).align_to(step1_ex2, LEFT)
        step4_ex2 = MathTex(r"\text{3. Set up equation and solve:}", color=COLOR_STEP).scale(0.8).next_to(step3_ex2, DOWN, buff=0.5).align_to(step1_ex2, LEFT)

        self.play(Write(step1_ex2))
        self.play(Write(step2_ex2))
        self.play(Write(step3_ex2))
        self.play(Write(step4_ex2))
        self.wait(1)

        calc1_ex2 = MathTex(r"\cos(\theta) = \frac{\text{Adjacent}}{\text{Hypotenuse}}", color=COLOR_CALCULATION).scale(0.9).next_to(step4_ex2, DOWN, buff=0.3).align_to(step4_ex2, LEFT)
        calc2_ex2 = MathTex(r"\cos(\theta) = \frac{8}{10}", color=COLOR_CALCULATION).scale(0.9).next_to(calc1_ex2, DOWN, buff=0.2).align_to(calc1_ex2, LEFT)
        calc3_ex2 = MathTex(r"\cos(\theta) = 0.8", color=COLOR_CALCULATION).scale(0.9).next_to(calc2_ex2, DOWN, buff=0.2).align_to(calc1_ex2, LEFT)
        calc4_ex2 = MathTex(r"\theta = \arccos(0.8)", color=COLOR_CALCULATION).scale(0.9).next_to(calc3_ex2, DOWN, buff=0.2).align_to(calc1_ex2, LEFT)
        result_ex2 = MathTex(r"\theta \approx 36.87^\circ", color=COLOR_RESULT).scale(1.2).next_to(calc4_ex2, DOWN, buff=0.5).align_to(calc1_ex2, LEFT)

        self.play(Write(calc1_ex2))
        self.play(TransformMatchingTex(calc1_ex2.copy(), calc2_ex2))
        self.play(TransformMatchingTex(calc2_ex2.copy(), calc3_ex2))
        self.play(TransformMatchingTex(calc3_ex2.copy(), calc4_ex2))
        self.play(TransformMatchingTex(calc4_ex2.copy(), result_ex2))
        self.wait(2)

        all_elements_scene5 = VGroup(
            example_title2, triangle_ex2, right_angle_square_ex2, angle_unknown_ex2, angle_arc_ex2,
            hypotenuse_value_ex2, opposite_label_ex2, adjacent_value_ex2,
            step1_ex2, step2_ex2, step3_ex2, step4_ex2,
            calc1_ex2, calc2_ex2, calc3_ex2, calc4_ex2, result_ex2
        )
        self.play(FadeOut(all_elements_scene5))
        self.wait(0.5)

        # --- Scene 6: Example 3 - Real-World Application ---
        self.clear()

        example_title3 = MathTex(r"\text{Example 3: Real-World Application}", color=COLOR_EXAMPLE_TITLE).scale(1.2).to_edge(UP, buff=0.7)
        self.play(Write(example_title3))
        self.wait(0.5)

        # Scenario: Ladder against a wall
        ground = Line(LEFT * 6, RIGHT * 0, color=COLOR_ADJACENT, stroke_width=4).shift(DOWN * 2)
        wall = Line(LEFT * 6, LEFT * 6 + UP * 4, color=COLOR_OPPOSITE, stroke_width=4).shift(DOWN * 2)
        ladder = Line(LEFT * 6 + UP * 4 + DOWN * 2, RIGHT * 0 + DOWN * 2, color=COLOR_HYPOTENUSE, stroke_width=4)

        ground_label = MathTex(r"\text{Ground}", color=COLOR_ADJACENT).next_to(ground, DOWN, buff=0.2)
        wall_label = MathTex(r"\text{Wall}", color=COLOR_OPPOSITE).next_to(wall, LEFT, buff=0.2)
        ladder_label = MathTex(r"\text{Ladder}", color=COLOR_HYPOTENUSE).next_to(ladder, UP + RIGHT, buff=0.2)

        right_angle_square_rw = Square(side_length=0.4, color=COLOR_RIGHT_ANGLE, fill_opacity=0.8).move_to(LEFT * 6 + DOWN * 2 + RIGHT * 0.2 + UP * 0.2)

        self.play(Create(ground), Create(wall), Create(ladder))
        self.play(Write(ground_label), Write(wall_label), Write(ladder_label))
        self.play(Create(right_angle_square_rw))
        self.wait(1)

        # Add values and unknown angle
        ladder_length = MathTex(r"5 \text{m}", color=COLOR_HYPOTENUSE).next_to(ladder, UP + RIGHT, buff=0.2)
        distance_from_wall = MathTex(r"3 \text{m}", color=COLOR_ADJACENT).next_to(ground, DOWN, buff=0.2)
        angle_theta_rw = MathTex(r"\theta", color=COLOR_ANGLE).move_to(ground.get_start() + RIGHT * 0.7 + UP * 0.4)
        angle_arc_rw = Angle(ground, ladder, radius=0.7, color=COLOR_ANGLE, other_angle=False)

        self.play(Transform(ladder_label, ladder_length), Transform(ground_label, distance_from_wall))
        self.play(Create(angle_arc_rw), Write(angle_theta_rw))
        self.wait(1)

        # Steps for solving
        step1_ex3 = MathTex(r"\text{1. Identify knowns: Adjacent } 3 \text{m, Hypotenuse } 5 \text{m.}", color=COLOR_STEP).scale(0.8).to_edge(RIGHT, buff=0.5).shift(UP*2.5)
        step2_ex3 = MathTex(r"\text{   Unknown: Angle } \theta \text{ (with the ground).}", color=COLOR_STEP).scale(0.8).next_to(step1_ex3, DOWN, buff=0.2).align_to(step1_ex3, LEFT)
        step3_ex3 = MathTex(r"\text{2. Choose ratio: Adjacent and Hypotenuse } \Rightarrow \text{ CAH (Cosine)}", color=COLOR_STEP).scale(0.8).next_to(step2_ex3, DOWN, buff=0.5).align_to(step1_ex3, LEFT)
        step4_ex3 = MathTex(r"\text{3. Set up equation and solve:}", color=COLOR_STEP).scale(0.8).next_to(step3_ex3, DOWN, buff=0.5).align_to(step1_ex3, LEFT)

        self.play(Write(step1_ex3))
        self.play(Write(step2_ex3))
        self.play(Write(step3_ex3))
        self.play(Write(step4_ex3))
        self.wait(1)

        calc1_ex3 = MathTex(r"\cos(\theta) = \frac{\text{Adjacent}}{\text{Hypotenuse}}", color=COLOR_CALCULATION).scale(0.9).next_to(step4_ex3, DOWN, buff=0.3).align_to(step4_ex3, LEFT)
        calc2_ex3 = MathTex(r"\cos(\theta) = \frac{3}{5}", color=COLOR_CALCULATION).scale(0.9).next_to(calc1_ex3, DOWN, buff=0.2).align_to(calc1_ex3, LEFT)
        calc3_ex3 = MathTex(r"\cos(\theta) = 0.6", color=COLOR_CALCULATION).scale(0.9).next_to(calc2_ex3, DOWN, buff=0.2).align_to(calc1_ex3, LEFT)
        calc4_ex3 = MathTex(r"\theta = \arccos(0.6)", color=COLOR_CALCULATION).scale(0.9).next_to(calc3_ex3, DOWN, buff=0.2).align_to(calc1_ex3, LEFT)
        result_ex3 = MathTex(r"\theta \approx 53.13^\circ", color=COLOR_RESULT).scale(1.2).next_to(calc4_ex3, DOWN, buff=0.5).align_to(calc1_ex3, LEFT)

        self.play(Write(calc1_ex3))
        self.play(TransformMatchingTex(calc1_ex3.copy(), calc2_ex3))
        self.play(TransformMatchingTex(calc2_ex3.copy(), calc3_ex3))
        self.play(TransformMatchingTex(calc3_ex3.copy(), calc4_ex3))
        self.play(TransformMatchingTex(calc4_ex3.copy(), result_ex3))
        self.wait(3)

        all_elements_scene6 = VGroup(
            example_title3, ground, wall, ladder, ladder_length, distance_from_wall,
            right_angle_square_rw, angle_theta_rw, angle_arc_rw,
            step1_ex3, step2_ex3, step3_ex3, step4_ex3,
            calc1_ex3, calc2_ex3, calc3_ex3, calc4_ex3, result_ex3
        )
        self.play(FadeOut(all_elements_scene6))
        self.wait(1)
