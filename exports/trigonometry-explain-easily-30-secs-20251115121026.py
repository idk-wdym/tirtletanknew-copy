from manim import *

# Configure Manim for 1920x1080 resolution at 30 FPS and white background
config.background_color = WHITE
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

class GeneratedScene(Scene):
    def construct(self):
        # --- Scene 1: Introduction to Trigonometry ---
        title = MathTex(r"\text{What is Trigonometry?}", color=BLACK).scale(1.5)
        self.play(Write(title))
        self.wait(1)

        intro_text = MathTex(
            r"\text{The study of relationships between angles and sides of triangles.}",
            color=BLACK
        ).scale(0.8).next_to(title, DOWN, buff=0.8)
        self.play(Write(intro_text))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(intro_text))
        self.wait(0.5)

        # Define points for a right-angled triangle
        p1 = LEFT * 3 + DOWN * 2  # Right angle vertex
        p2 = RIGHT * 1 + DOWN * 2  # Angle theta vertex
        p3 = LEFT * 3 + UP * 1    # Third vertex

        triangle = Polygon(p1, p2, p3, color=BLUE, fill_opacity=0.2, stroke_width=4)
        
        # Mark the right angle
        right_angle_marker = VGroup(
            Line(p1 + RIGHT * 0.3, p1 + RIGHT * 0.3 + UP * 0.3, color=BLUE),
            Line(p1 + UP * 0.3, p1 + RIGHT * 0.3 + UP * 0.3, color=BLUE)
        )

        self.play(Create(triangle), Create(right_angle_marker))
        self.wait(0.5)

        # Label the angle theta
        theta = MathTex(r"\theta", color=YELLOW).scale(0.8).move_to(p2 + LEFT * 0.5 + UP * 0.3)
        angle_arc = Arc(radius=0.6, start_angle=PI, angle=-PI/2, arc_center=p2, color=YELLOW)
        self.play(Create(angle_arc), Write(theta))
        self.wait(0.5)

        # Label sides: Hypotenuse, Opposite, Adjacent
        hypotenuse_label = MathTex(r"\text{Hypotenuse}", color=GREEN).scale(0.7).next_to(Line(p2, p3), UP + RIGHT, buff=0.2)
        opposite_label = MathTex(r"\text{Opposite}", color=RED).scale(0.7).next_to(Line(p1, p3), LEFT, buff=0.2)
        adjacent_label = MathTex(r"\text{Adjacent}", color=PURPLE).scale(0.7).next_to(Line(p1, p2), DOWN, buff=0.2)

        self.play(
            Write(hypotenuse_label),
            Write(opposite_label),
            Write(adjacent_label)
        )
        self.wait(2)

        # --- Scene 2: SOH CAH TOA ---
        self.play(
            FadeOut(triangle), FadeOut(right_angle_marker), FadeOut(angle_arc), FadeOut(theta),
            FadeOut(hypotenuse_label), FadeOut(opposite_label), FadeOut(adjacent_label)
        )
        self.wait(0.5)

        soh_cah_toa_title = MathTex(r"\text{SOH CAH TOA}", color=BLACK).scale(1.5).to_edge(UP)
        self.play(Write(soh_cah_toa_title))
        self.wait(1)

        # Display the trigonometric ratios
        soh = MathTex(r"\text{SOH: } \sin(\theta) = \frac{\text{Opposite}}{\text{Hypotenuse}}", color=BLUE_C).scale(1.0).shift(UP*1.5 + LEFT*3)
        cah = MathTex(r"\text{CAH: } \cos(\theta) = \frac{\text{Adjacent}}{\text{Hypotenuse}}", color=GREEN_C).scale(1.0).shift(DOWN*0.5 + LEFT*3)
        toa = MathTex(r"\text{TOA: } \tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}", color=RED_C).scale(1.0).shift(DOWN*2.5 + LEFT*3)

        self.play(Write(soh))
        self.wait(1)
        self.play(Write(cah))
        self.wait(1)
        self.play(Write(toa))
        self.wait(2)

        # --- Scene 3: Example 1 - Sine ---
        self.play(FadeOut(soh_cah_toa_title), FadeOut(cah), FadeOut(toa))
        self.wait(0.5)

        example_title_1 = MathTex(r"\text{Example 1: Sine}", color=BLACK).scale(1.2).to_edge(UP)
        # Transform the SOH formula into the new title for a smooth transition
        self.play(Transform(soh, example_title_1)) 
        self.wait(1)

        # Redraw triangle with specific values for the example
        p1_ex = LEFT * 3 + DOWN * 2
        p2_ex = RIGHT * 1 + DOWN * 2
        p3_ex = LEFT * 3 + UP * 1

        triangle_ex = Polygon(p1_ex, p2_ex, p3_ex, color=BLUE, fill_opacity=0.2, stroke_width=4)
        right_angle_marker_ex = VGroup(
            Line(p1_ex + RIGHT * 0.3, p1_ex + RIGHT * 0.3 + UP * 0.3, color=BLUE),
            Line(p1_ex + UP * 0.3, p1_ex + RIGHT * 0.3 + UP * 0.3, color=BLUE)
        )
        self.play(Create(triangle_ex), Create(right_angle_marker_ex))

        # Side lengths and angle for the example
        opposite_val = MathTex(r"3", color=RED).scale(0.8).next_to(Line(p1_ex, p3_ex), LEFT, buff=0.2)
        adjacent_val = MathTex(r"4", color=PURPLE).scale(0.8).next_to(Line(p1_ex, p2_ex), DOWN, buff=0.2)
        hypotenuse_val = MathTex(r"5", color=GREEN).scale(0.8).next_to(Line(p2_ex, p3_ex), UP + RIGHT, buff=0.2)

        theta_ex = MathTex(r"\theta", color=YELLOW).scale(0.8).move_to(p2_ex + LEFT * 0.5 + UP * 0.3)
        angle_arc_ex = Arc(radius=0.6, start_angle=PI, angle=-PI/2, arc_center=p2_ex, color=YELLOW)

        self.play(
            Create(angle_arc_ex), Write(theta_ex),
            Write(opposite_val), Write(adjacent_val), Write(hypotenuse_val)
        )
        self.wait(1)

        # Highlight the relevant sides for Sine (Opposite and Hypotenuse)
        self.play(
            Indicate(Line(p1_ex, p3_ex), color=RED, scale_factor=1.2),
            Indicate(Line(p2_ex, p3_ex), color=GREEN, scale_factor=1.2),
            Indicate(theta_ex, color=YELLOW)
        )
        self.wait(1)

        sine_formula = MathTex(r"\sin(\theta) = \frac{\text{Opposite}}{\text{Hypotenuse}}", color=BLUE_C).scale(0.9).next_to(triangle_ex, RIGHT, buff=1).align_to(example_title_1, UP)
        sine_calc = MathTex(r"\sin(\theta) = \frac{3}{5} = 0.6", color=BLUE_C).scale(0.9).next_to(sine_formula, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(Write(sine_formula))
        self.wait(1)
        self.play(Write(sine_calc))
        self.wait(2)

        # --- Scene 4: Example 2 - Cosine ---
        self.play(
            FadeOut(triangle_ex), FadeOut(right_angle_marker_ex), FadeOut(angle_arc_ex), FadeOut(theta_ex),
            FadeOut(opposite_val), FadeOut(adjacent_val), FadeOut(hypotenuse_val),
            FadeOut(sine_formula), FadeOut(sine_calc)
        )
        self.wait(0.5)

        example_title_2 = MathTex(r"\text{Example 2: Cosine}", color=BLACK).scale(1.2).to_edge(UP)
        # Transform the previous title to the new one
        self.play(Transform(soh, example_title_2)) 
        self.wait(1)

        # Redraw triangle with specific values (same as before)
        triangle_ex_2 = Polygon(p1_ex, p2_ex, p3_ex, color=BLUE, fill_opacity=0.2, stroke_width=4)
        right_angle_marker_ex_2 = VGroup(
            Line(p1_ex + RIGHT * 0.3, p1_ex + RIGHT * 0.3 + UP * 0.3, color=BLUE),
            Line(p1_ex + UP * 0.3, p1_ex + RIGHT * 0.3 + UP * 0.3, color=BLUE)
        )
        self.play(Create(triangle_ex_2), Create(right_angle_marker_ex_2))

        opposite_val_2 = MathTex(r"3", color=RED).scale(0.8).next_to(Line(p1_ex, p3_ex), LEFT, buff=0.2)
        adjacent_val_2 = MathTex(r"4", color=PURPLE).scale(0.8).next_to(Line(p1_ex, p2_ex), DOWN, buff=0.2)
        hypotenuse_val_2 = MathTex(r"5", color=GREEN).scale(0.8).next_to(Line(p2_ex, p3_ex), UP + RIGHT, buff=0.2)

        theta_ex_2 = MathTex(r"\theta", color=YELLOW).scale(0.8).move_to(p2_ex + LEFT * 0.5 + UP * 0.3)
        angle_arc_ex_2 = Arc(radius=0.6, start_angle=PI, angle=-PI/2, arc_center=p2_ex, color=YELLOW)

        self.play(
            Create(angle_arc_ex_2), Write(theta_ex_2),
            Write(opposite_val_2), Write(adjacent_val_2), Write(hypotenuse_val_2)
        )
        self.wait(1)

        # Highlight the relevant sides for Cosine (Adjacent and Hypotenuse)
        self.play(
            Indicate(Line(p1_ex, p2_ex), color=PURPLE, scale_factor=1.2),
            Indicate(Line(p2_ex, p3_ex), color=GREEN, scale_factor=1.2),
            Indicate(theta_ex_2, color=YELLOW)
        )
        self.wait(1)

        cosine_formula = MathTex(r"\cos(\theta) = \frac{\text{Adjacent}}{\text{Hypotenuse}}", color=GREEN_C).scale(0.9).next_to(triangle_ex_2, RIGHT, buff=1).align_to(example_title_2, UP)
        cosine_calc = MathTex(r"\cos(\theta) = \frac{4}{5} = 0.8", color=GREEN_C).scale(0.9).next_to(cosine_formula, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(Write(cosine_formula))
        self.wait(1)
        self.play(Write(cosine_calc))
        self.wait(2)

        # --- Scene 5: Example 3 - Tangent ---
        self.play(
            FadeOut(triangle_ex_2), FadeOut(right_angle_marker_ex_2), FadeOut(angle_arc_ex_2), FadeOut(theta_ex_2),
            FadeOut(opposite_val_2), FadeOut(adjacent_val_2), FadeOut(hypotenuse_val_2),
            FadeOut(cosine_formula), FadeOut(cosine_calc)
        )
        self.wait(0.5)

        example_title_3 = MathTex(r"\text{Example 3: Tangent}", color=BLACK).scale(1.2).to_edge(UP)
        # Transform the previous title to the new one
        self.play(Transform(soh, example_title_3)) 
        self.wait(1)

        # Redraw triangle with specific values (same as before)
        triangle_ex_3 = Polygon(p1_ex, p2_ex, p3_ex, color=BLUE, fill_opacity=0.2, stroke_width=4)
        right_angle_marker_ex_3 = VGroup(
            Line(p1_ex + RIGHT * 0.3, p1_ex + RIGHT * 0.3 + UP * 0.3, color=BLUE),
            Line(p1_ex + UP * 0.3, p1_ex + RIGHT * 0.3 + UP * 0.3, color=BLUE)
        )
        self.play(Create(triangle_ex_3), Create(right_angle_marker_ex_3))

        opposite_val_3 = MathTex(r"3", color=RED).scale(0.8).next_to(Line(p1_ex, p3_ex), LEFT, buff=0.2)
        adjacent_val_3 = MathTex(r"4", color=PURPLE).scale(0.8).next_to(Line(p1_ex, p2_ex), DOWN, buff=0.2)
        hypotenuse_val_3 = MathTex(r"5", color=GREEN).scale(0.8).next_to(Line(p2_ex, p3_ex), UP + RIGHT, buff=0.2)

        theta_ex_3 = MathTex(r"\theta", color=YELLOW).scale(0.8).move_to(p2_ex + LEFT * 0.5 + UP * 0.3)
        angle_arc_ex_3 = Arc(radius=0.6, start_angle=PI, angle=-PI/2, arc_center=p2_ex, color=YELLOW)

        self.play(
            Create(angle_arc_ex_3), Write(theta_ex_3),
            Write(opposite_val_3), Write(adjacent_val_3), Write(hypotenuse_val_3)
        )
        self.wait(1)

        # Highlight the relevant sides for Tangent (Opposite and Adjacent)
        self.play(
            Indicate(Line(p1_ex, p3_ex), color=RED, scale_factor=1.2),
            Indicate(Line(p1_ex, p2_ex), color=PURPLE, scale_factor=1.2),
            Indicate(theta_ex_3, color=YELLOW)
        )
        self.wait(1)

        tangent_formula = MathTex(r"\tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}", color=RED_C).scale(0.9).next_to(triangle_ex_3, RIGHT, buff=1).align_to(example_title_3, UP)
        tangent_calc = MathTex(r"\tan(\theta) = \frac{3}{4} = 0.75", color=RED_C).scale(0.9).next_to(tangent_formula, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(Write(tangent_formula))
        self.wait(1)
        self.play(Write(tangent_calc))
        self.wait(2)

        # Clear the screen after all examples
        self.play(
            FadeOut(triangle_ex_3), FadeOut(right_angle_marker_ex_3), FadeOut(angle_arc_ex_3), FadeOut(theta_ex_3),
            FadeOut(opposite_val_3), FadeOut(adjacent_val_3), FadeOut(hypotenuse_val_3),
            FadeOut(tangent_formula), FadeOut(tangent_calc), FadeOut(soh) # Fade out the last transformed title
        )
        self.wait(1)

        # Final summary
        summary_text = MathTex(
            r"\text{Trigonometry helps us find unknown sides and angles}",
            r"\\",
            r"\text{in right-angled triangles using SOH CAH TOA.}",
            color=BLACK
        ).scale(1.0)
        self.play(Write(summary_text))
        self.wait(3)
        self.play(FadeOut(summary_text))
        self.wait(1)