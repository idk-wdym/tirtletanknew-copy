from manim import *

config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

class GeneratedScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # --- Scene 1: Introduction to Trigonometry ---
        title = MathTex(r"\text{三角学 (Trigonometry)}", color=BLACK, font_size=72)
        definition = MathTex(
            r"\text{研究三角形中边和角之间关系的数学分支。}",
            color=BLACK,
            font_size=48
        )
        definition.next_to(title, DOWN, buff=0.8)

        self.play(Write(title))
        self.play(Write(definition))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(definition))
        self.wait(0.5)

        # --- Scene 2: Right-angled Triangle Basics ---
        right_angle_text = MathTex(r"\text{直角三角形是关键}", color=BLUE_D, font_size=60)
        right_angle_text.to_edge(UP, buff=0.8)
        self.play(Write(right_angle_text))
        self.wait(1)

        # Draw a right-angled triangle
        p1 = LEFT * 4 + DOWN * 2
        p2 = RIGHT * 2 + DOWN * 2
        p3 = LEFT * 4 + UP * 2

        triangle = Polygon(p1, p2, p3, color=BLUE, fill_opacity=0.2)
        right_angle_square = Square(side_length=0.4, color=BLUE, fill_opacity=1)
        right_angle_square.move_to(p1 + RIGHT * 0.2 + UP * 0.2)

        # Labels for vertices
        label_A = MathTex(r"A", color=BLACK).next_to(p3, UP + LEFT * 0.2)
        label_B = MathTex(r"B", color=BLACK).next_to(p2, RIGHT)
        label_C = MathTex(r"C", color=BLACK).next_to(p1, DOWN + LEFT * 0.2)

        # Angle theta
        angle_theta = Angle(Line(p1, p2), Line(p1, p3), radius=0.7, color=RED)
        label_theta = MathTex(r"\theta", color=RED).move_to(angle_theta.get_center() + RIGHT * 0.3 + UP * 0.1)

        self.play(Create(triangle), Create(right_angle_square))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.play(Create(angle_theta), Write(label_theta))
        self.wait(1)

        # Label sides relative to theta
        hypotenuse_label = MathTex(r"\text{斜边}", color=GREEN_D).next_to(Line(p3, p2), UP * 0.5 + RIGHT * 0.5)
        opposite_label = MathTex(r"\text{对边}", color=PURPLE_D).next_to(Line(p1, p3), LEFT * 0.5)
        adjacent_label = MathTex(r"\text{邻边}", color=ORANGE_D).next_to(Line(p1, p2), DOWN * 0.5)

        self.play(Write(hypotenuse_label))
        self.play(Write(opposite_label))
        self.play(Write(adjacent_label))
        self.wait(2)

        self.play(
            FadeOut(right_angle_text),
            FadeOut(triangle),
            FadeOut(right_angle_square),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(label_C),
            FadeOut(angle_theta),
            FadeOut(label_theta),
            FadeOut(hypotenuse_label),
            FadeOut(opposite_label),
            FadeOut(adjacent_label)
        )
        self.wait(0.5)

        # --- Scene 3: SOH CAH TOA Definitions ---
        soh_cah_toa_title = MathTex(r"\text{SOH CAH TOA}", color=BLUE_D, font_size=72)
        soh_cah_toa_title.to_edge(UP, buff=0.8)
        self.play(Write(soh_cah_toa_title))
        self.wait(1)

        # Sine definition
        sine_text = MathTex(r"\text{正弦 (Sine)}", color=RED_E, font_size=50).to_edge(LEFT, buff=1).shift(UP*1.5)
        sine_formula = MathTex(r"\sin(\theta) = \frac{\text{对边}}{\text{斜边}}", color=RED_E, font_size=50).next_to(sine_text, RIGHT, buff=1)
        self.play(Write(sine_text), Write(sine_formula))
        self.wait(1.5)

        # Cosine definition
        cosine_text = MathTex(r"\text{余弦 (Cosine)}", color=GREEN_E, font_size=50).to_edge(LEFT, buff=1).shift(DOWN*0.5)
        cosine_formula = MathTex(r"\cos(\theta) = \frac{\text{邻边}}{\text{斜边}}", color=GREEN_E, font_size=50).next_to(cosine_text, RIGHT, buff=1)
        self.play(Write(cosine_text), Write(cosine_formula))
        self.wait(1.5)

        # Tangent definition
        tangent_text = MathTex(r"\text{正切 (Tangent)}", color=PURPLE_E, font_size=50).to_edge(LEFT, buff=1).shift(DOWN*2.5)
        tangent_formula = MathTex(r"\tan(\theta) = \frac{\text{对边}}{\text{邻边}}", color=PURPLE_E, font_size=50).next_to(tangent_text, RIGHT, buff=1)
        self.play(Write(tangent_text), Write(tangent_formula))
        self.wait(2)

        self.play(
            FadeOut(soh_cah_toa_title),
            FadeOut(sine_text), FadeOut(sine_formula),
            FadeOut(cosine_text), FadeOut(cosine_formula),
            FadeOut(tangent_text), FadeOut(tangent_formula)
        )
        self.wait(0.5)

        # --- Scene 4: Example Calculation ---
        example_title = MathTex(r"\text{例子 (Example)}", color=BLUE_D, font_size=60)
        example_title.to_edge(UP, buff=0.8)
        self.play(Write(example_title))
        self.wait(1)

        # Draw a new right-angled triangle with specific side lengths
        p1_ex = LEFT * 4 + DOWN * 2
        p2_ex = RIGHT * 0 + DOWN * 2
        p3_ex = LEFT * 4 + UP * 1

        triangle_ex = Polygon(p1_ex, p2_ex, p3_ex, color=BLUE, fill_opacity=0.2)
        right_angle_square_ex = Square(side_length=0.4, color=BLUE, fill_opacity=1)
        right_angle_square_ex.move_to(p1_ex + RIGHT * 0.2 + UP * 0.2)

        # Side lengths
        side_3 = MathTex(r"3", color=PURPLE_D).next_to(Line(p1_ex, p3_ex), LEFT * 0.5)
        side_4 = MathTex(r"4", color=ORANGE_D).next_to(Line(p1_ex, p2_ex), DOWN * 0.5)
        side_5 = MathTex(r"5", color=GREEN_D).next_to(Line(p3_ex, p2_ex), UP * 0.5 + RIGHT * 0.5)

        # Angle theta
        angle_theta_ex = Angle(Line(p1_ex, p2_ex), Line(p1_ex, p3_ex), radius=0.7, color=RED)
        label_theta_ex = MathTex(r"\theta", color=RED).move_to(angle_theta_ex.get_center() + RIGHT * 0.3 + UP * 0.1)

        self.play(Create(triangle_ex), Create(right_angle_square_ex))
        self.play(Write(side_3), Write(side_4), Write(side_5))
        self.play(Create(angle_theta_ex), Write(label_theta_ex))
        self.wait(1.5)

        # Calculate ratios for the example
        calc_sine = MathTex(r"\sin(\theta) = \frac{\text{对边}}{\text{斜边}} = \frac{3}{5}", color=RED_E, font_size=45).to_edge(RIGHT, buff=1).shift(UP*1.5)
        calc_cosine = MathTex(r"\cos(\theta) = \frac{\text{邻边}}{\text{斜边}} = \frac{4}{5}", color=GREEN_E, font_size=45).to_edge(RIGHT, buff=1).shift(DOWN*0.5)
        calc_tangent = MathTex(r"\tan(\theta) = \frac{\text{对边}}{\text{邻边}} = \frac{3}{4}", color=PURPLE_E, font_size=45).to_edge(RIGHT, buff=1).shift(DOWN*2.5)

        self.play(Write(calc_sine))
        self.wait(1)
        self.play(Write(calc_cosine))
        self.wait(1)
        self.play(Write(calc_tangent))
        self.wait(2)

        self.play(
            FadeOut(example_title),
            FadeOut(triangle_ex),
            FadeOut(right_angle_square_ex),
            FadeOut(side_3), FadeOut(side_4), FadeOut(side_5),
            FadeOut(angle_theta_ex), FadeOut(label_theta_ex),
            FadeOut(calc_sine), FadeOut(calc_cosine), FadeOut(calc_tangent)
        )
        self.wait(1)

        # --- Scene 5: Final Recap ---
        recap_text = MathTex(r"\text{三角学：理解直角三角形的边角关系}", color=BLUE_D, font_size=60)
        recap_text.to_edge(UP, buff=0.8)
        self.play(Write(recap_text))

        final_formulas = VGroup(
            MathTex(r"\sin(\theta) = \frac{\text{对边}}{\text{斜边}}", color=RED_E, font_size=50),
            MathTex(r"\cos(\theta) = \frac{\text{邻边}}{\text{斜边}}", color=GREEN_E, font_size=50),
            MathTex(r"\tan(\theta) = \frac{\text{对边}}{\text{邻边}}", color=PURPLE_E, font_size=50)
        ).arrange(DOWN, buff=0.8)
        self.play(Write(final_formulas))
        self.wait(3)

        self.play(FadeOut(recap_text), FadeOut(final_formulas))
        self.wait(1)