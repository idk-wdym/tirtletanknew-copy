from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Configure resolution and background
        self.camera.background_color = WHITE
        # Manim's default frame_width and frame_height are 16x9, suitable for 1920x1080.
        # No explicit setting needed unless a different aspect ratio is desired.

        # --- Scene 1: Introduction to Trigonometry ---
        title = MathTex(r"\text{What is Trigonometry?}", color=BLUE_E)
        title.scale(1.5)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        intro_text = MathTex(
            r"\text{Trigonometry studies relationships between angles and sides of triangles,}",
            r"\\ \text{especially right-angled triangles.}",
            color=TEAL_E
        )
        intro_text.next_to(title, DOWN, buff=0.8)
        self.play(Write(intro_text))
        self.wait(1)

        # Create a right-angled triangle
        p1 = LEFT * 3 + DOWN * 2 # Right angle vertex
        p2 = RIGHT * 3 + DOWN * 2 # Angle theta vertex
        p3 = LEFT * 3 + UP * 2 # Remaining vertex

        triangle = Polygon(p1, p2, p3, color=BLACK, fill_opacity=0.2, fill_color=LIGHT_GRAY)
        right_angle_square = Square(side_length=0.4, color=BLACK).move_to(p1, UL).shift(RIGHT * 0.2 + UP * 0.2)

        # Label the angle theta at p2
        line_adj_s1 = Line(p2, p1)
        line_hyp_s1 = Line(p2, p3)
        angle_arc_s1 = Angle(line_adj_s1, line_hyp_s1, radius=0.7, color=PURPLE_E)
        theta_label_s1 = MathTex(r"\theta", color=PURPLE_E).next_to(angle_arc_s1, DR, buff=0.1)

        self.play(
            Create(triangle),
            Create(right_angle_square),
            run_time=1.5
        )
        self.play(
            Create(angle_arc_s1),
            Write(theta_label_s1)
        )
        self.wait(0.5)

        # Label the sides relative to theta
        hypotenuse_label_s1 = MathTex(r"\text{Hypotenuse}", color=RED_E).next_to(Line(p2, p3), UP + RIGHT, buff=0.2)
        opposite_label_s1 = MathTex(r"\text{Opposite}", color=GREEN_E).next_to(Line(p1, p3), LEFT, buff=0.2)
        adjacent_label_s1 = MathTex(r"\text{Adjacent}", color=YELLOW_E).next_to(Line(p1, p2), DOWN, buff=0.2)

        self.play(
            Write(hypotenuse_label_s1),
            Write(opposite_label_s1),
            Write(adjacent_label_s1)
        )
        self.wait(1)

        # Introduce SOH CAH TOA
        soh_cah_toa = MathTex(
            r"\text{SOH: } \sin(\theta) = \frac{\text{Opposite}}{\text{Hypotenuse}}",
            r"\\ \text{CAH: } \cos(\theta) = \frac{\text{Adjacent}}{\text{Hypotenuse}}",
            r"\\ \text{TOA: } \tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}",
            color=ORANGE_E
        )
        soh_cah_toa.scale(0.9)
        soh_cah_toa.next_to(triangle, RIGHT, buff=1.5).shift(UP*0.5)
        self.play(Write(soh_cah_toa))
        self.wait(2.5)

        # Clear screen for next section
        self.play(FadeOut(title, intro_text, triangle, right_angle_square, angle_arc_s1, theta_label_s1,
                           hypotenuse_label_s1, opposite_label_s1, adjacent_label_s1, soh_cah_toa))
        self.wait(0.5)

        # --- Scene 2: Example 1 - Finding a Side ---
        example1_title = MathTex(r"\text{Example 1: Finding a Side}", color=BLUE_E)
        example1_title.scale(1.3)
        example1_title.to_edge(UP)
        self.play(Write(example1_title))
        self.wait(0.5)

        # Create a new triangle for the example
        p1_ex1 = LEFT * 3 + DOWN * 2 # Right angle vertex
        p2_ex1 = RIGHT * 1 + DOWN * 2 # Angle vertex
        p3_ex1 = LEFT * 3 + UP * 1.5 # Remaining vertex

        triangle_ex1 = Polygon(p1_ex1, p2_ex1, p3_ex1, color=BLACK, fill_opacity=0.2, fill_color=LIGHT_GRAY)
        right_angle_square_ex1 = Square(side_length=0.4, color=BLACK).move_to(p1_ex1, UL).shift(RIGHT * 0.2 + UP * 0.2)

        # Knowns: Angle and Hypotenuse
        line_adj_ex1 = Line(p2_ex1, p1_ex1)
        line_hyp_ex1 = Line(p2_ex1, p3_ex1)
        angle_arc_ex1 = Angle(line_adj_ex1, line_hyp_ex1, radius=0.7, color=PURPLE_E)
        angle_label_ex1 = MathTex(r"30^\circ", color=PURPLE_E).next_to(angle_arc_ex1, DR, buff=0.1)

        hyp_label_ex1 = MathTex(r"5", color=RED_E).next_to(Line(p2_ex1, p3_ex1), UP + RIGHT, buff=0.2)

        # Unknown: Opposite side
        opp_label_ex1 = MathTex(r"x", color=GREEN_E).next_to(Line(p1_ex1, p3_ex1), LEFT, buff=0.2)

        self.play(
            Create(triangle_ex1),
            Create(right_angle_square_ex1)
        )
        self.play(
            Create(angle_arc_ex1),
            Write(angle_label_ex1),
            Write(hyp_label_ex1),
            Write(opp_label_ex1)
        )
        self.wait(0.5)

        question_text_ex1 = MathTex(r"\text{Find the length of side } x.", color=TEAL_E)
        question_text_ex1.next_to(example1_title, DOWN, buff=0.8)
        self.play(Write(question_text_ex1))
        self.wait(0.5)

        # Solution steps
        step1_ex1 = MathTex(r"\text{1. Knowns: Angle } = 30^\circ, \text{ Hypotenuse } = 5.", color=BLUE_E)
        step1_ex1.to_edge(LEFT).shift(UP*1.5)
        self.play(Write(step1_ex1))
        self.wait(0.5)

        step2_ex1 = MathTex(r"\text{2. Unknown: Opposite side } x.", color=BLUE_E)
        step2_ex1.next_to(step1_ex1, DOWN, aligned_edge=LEFT)
        self.play(Write(step2_ex1))
        self.wait(0.5)

        step3_ex1 = MathTex(r"\text{3. Ratio: Opposite and Hypotenuse } \implies \text{SOH (Sine)}", color=BLUE_E)
        step3_ex1.next_to(step2_ex1, DOWN, aligned_edge=LEFT)
        self.play(Write(step3_ex1))
        self.wait(1.5)

        formula_ex1 = MathTex(r"\sin(\theta) = \frac{\text{Opposite}}{\text{Hypotenuse}}", color=ORANGE_E)
        formula_ex1.next_to(step3_ex1, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(formula_ex1))
        self.wait(0.5)

        substitute_ex1 = MathTex(r"\sin(30^\circ) = \frac{x}{5}", color=ORANGE_E)
        substitute_ex1.next_to(formula_ex1, DOWN, aligned_edge=LEFT)
        self.play(Write(substitute_ex1))
        self.wait(0.5)

        solve_ex1 = MathTex(r"x = 5 \times \sin(30^\circ)", color=ORANGE_E)
        solve_ex1.next_to(substitute_ex1, DOWN, aligned_edge=LEFT)
        self.play(Write(solve_ex1))
        self.wait(0.5)

        result_ex1 = MathTex(r"x = 5 \times 0.5", r"\\ x = 2.5", color=ORANGE_E)
        result_ex1.next_to(solve_ex1, DOWN, aligned_edge=LEFT)
        self.play(Write(result_ex1[0]))
        self.wait(0.5)
        self.play(Write(result_ex1[1]))
        self.wait(1.5)

        # Clear screen for next section
        self.play(FadeOut(example1_title, question_text_ex1, triangle_ex1, right_angle_square_ex1,
                           angle_arc_ex1, angle_label_ex1, hyp_label_ex1, opp_label_ex1,
                           step1_ex1, step2_ex1, step3_ex1, formula_ex1, substitute_ex1, solve_ex1, result_ex1))
        self.wait(0.5)

        # --- Scene 3: Example 2 - Finding an Angle ---
        example2_title = MathTex(r"\text{Example 2: Finding an Angle}", color=BLUE_E)
        example2_title.scale(1.3)
        example2_title.to_edge(UP)
        self.play(Write(example2_title))
        self.wait(0.5)

        # Create a new triangle for the example
        p1_ex2 = LEFT * 3 + DOWN * 2 # Right angle vertex
        p2_ex2 = RIGHT * 1 + DOWN * 2 # Angle vertex
        p3_ex2 = LEFT * 3 + UP * 1.5 # Remaining vertex

        triangle_ex2 = Polygon(p1_ex2, p2_ex2, p3_ex2, color=BLACK, fill_opacity=0.2, fill_color=LIGHT_GRAY)
        right_angle_square_ex2 = Square(side_length=0.4, color=BLACK).move_to(p1_ex2, UL).shift(RIGHT * 0.2 + UP * 0.2)

        # Knowns: Adjacent and Hypotenuse
        adj_label_ex2 = MathTex(r"4", color=YELLOW_E).next_to(Line(p1_ex2, p2_ex2), DOWN, buff=0.2)
        hyp_label_ex2 = MathTex(r"5", color=RED_E).next_to(Line(p2_ex2, p3_ex2), UP + RIGHT, buff=0.2)

        # Unknown: Angle
        line_adj_ex2 = Line(p2_ex2, p1_ex2)
        line_hyp_ex2 = Line(p2_ex2, p3_ex2)
        angle_arc_ex2 = Angle(line_adj_ex2, line_hyp_ex2, radius=0.7, color=PURPLE_E)
        angle_label_ex2 = MathTex(r"\theta", color=PURPLE_E).next_to(angle_arc_ex2, DR, buff=0.1)

        self.play(
            Create(triangle_ex2),
            Create(right_angle_square_ex2)
        )
        self.play(
            Create(angle_arc_ex2),
            Write(angle_label_ex2),
            Write(adj_label_ex2),
            Write(hyp_label_ex2)
        )
        self.wait(0.5)

        question_text_ex2 = MathTex(r"\text{Find the angle } \theta.", color=TEAL_E)
        question_text_ex2.next_to(example2_title, DOWN, buff=0.8)
        self.play(Write(question_text_ex2))
        self.wait(0.5)

        # Solution steps
        step1_ex2 = MathTex(r"\text{1. Knowns: Adjacent } = 4, \text{ Hypotenuse } = 5.", color=BLUE_E)
        step1_ex2.to_edge(LEFT).shift(UP*1.5)
        self.play(Write(step1_ex2))
        self.wait(0.5)

        step2_ex2 = MathTex(r"\text{2. Unknown: Angle } \theta.", color=BLUE_E)
        step2_ex2.next_to(step1_ex2, DOWN, aligned_edge=LEFT)
        self.play(Write(step2_ex2))
        self.wait(0.5)

        step3_ex2 = MathTex(r"\text{3. Ratio: Adjacent and Hypotenuse } \implies \text{CAH (Cosine)}", color=BLUE_E)
        step3_ex2.next_to(step2_ex2, DOWN, aligned_edge=LEFT)
        self.play(Write(step3_ex2))
        self.wait(1.5)

        formula_ex2 = MathTex(r"\cos(\theta) = \frac{\text{Adjacent}}{\text{Hypotenuse}}", color=ORANGE_E)
        formula_ex2.next_to(step3_ex2, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(formula_ex2))
        self.wait(0.5)

        substitute_ex2 = MathTex(r"\cos(\theta) = \frac{4}{5}", color=ORANGE_E)
        substitute_ex2.next_to(formula_ex2, DOWN, aligned_edge=LEFT)
        self.play(Write(substitute_ex2))
        self.wait(0.5)

        solve_ex2 = MathTex(r"\theta = \arccos\left(\frac{4}{5}\right)", color=ORANGE_E)
        solve_ex2.next_to(substitute_ex2, DOWN, aligned_edge=LEFT)
        self.play(Write(solve_ex2))
        self.wait(0.5)

        result_ex2 = MathTex(r"\theta \approx 36.87^\circ", color=ORANGE_E)
        result_ex2.next_to(solve_ex2, DOWN, aligned_edge=LEFT)
        self.play(Write(result_ex2))
        self.wait(1.5)

        # Clear screen for conclusion
        self.play(FadeOut(example2_title, question_text_ex2, triangle_ex2, right_angle_square_ex2,
                           angle_arc_ex2, angle_label_ex2, adj_label_ex2, hyp_label_ex2,
                           step1_ex2, step2_ex2, step3_ex2, formula_ex2, substitute_ex2, solve_ex2, result_ex2))
        self.wait(0.5)

        # --- Conclusion ---
        conclusion_text = MathTex(
            r"\text{Trigonometry is essential for solving problems involving triangles,}",
            r"\\ \text{from engineering to astronomy!}",
            color=BLUE_E
        )
        conclusion_text.scale(1.2)
        self.play(Write(conclusion_text))
        self.wait(2)
        self.play(FadeOut(conclusion_text))
        self.wait(0.5)