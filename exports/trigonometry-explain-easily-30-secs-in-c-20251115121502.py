from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Configure resolution and background
        self.camera.background_color = WHITE
        config.frame_width = 16
        config.frame_height = 9
        config.pixel_width = 1920
        config.pixel_height = 1080
        config.frame_rate = 30

        # --- Scene 1: Introduction and Definition ---
        title = MathTex(r"\text{三角学简介}", color=BLUE_D).scale(1.5).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.8)
        self.wait(0.3)

        definition_text = MathTex(
            r"\text{三角学：研究三角形的角和边之间的关系。}",
            color=BLACK
        ).scale(0.8).next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(definition_text, shift=UP), run_time=0.8)
        self.wait(0.3)

        # Draw a generic triangle and label angles/sides concurrently
        triangle_points = [
            LEFT * 3 + DOWN * 1.5,
            RIGHT * 3 + DOWN * 1.5,
            UP * 2
        ]
        generic_triangle = Polygon(*triangle_points, color=PURPLE, fill_opacity=0.3, stroke_width=5)
        
        angle_label_A = MathTex(r"\alpha", color=RED).move_to(triangle_points[0] + RIGHT * 0.5 + UP * 0.5)
        angle_label_B = MathTex(r"\beta", color=RED).move_to(triangle_points[1] + LEFT * 0.5 + UP * 0.5)
        angle_label_C = MathTex(r"\gamma", color=RED).move_to(triangle_points[2] + DOWN * 0.5)

        side_label_a = MathTex(r"\text{边a}", color=GREEN).move_to((triangle_points[1] + triangle_points[2]) / 2 + RIGHT * 0.5)
        side_label_b = MathTex(r"\text{边b}", color=GREEN).move_to((triangle_points[0] + triangle_points[2]) / 2 + LEFT * 0.5)
        side_label_c = MathTex(r"\text{边c}", color=GREEN).move_to((triangle_points[0] + triangle_points[1]) / 2 + DOWN * 0.5)

        self.play(
            Create(generic_triangle),
            FadeIn(angle_label_A, angle_label_B, angle_label_C, side_label_a, side_label_b, side_label_c),
            run_time=2
        )
        self.wait(0.5)

        self.play(
            FadeOut(title, definition_text, generic_triangle,
                    angle_label_A, angle_label_B, angle_label_C,
                    side_label_a, side_label_b, side_label_c),
            run_time=0.8
        )
        self.clear()

        # --- Scene 2: Right Triangles and Terminology ---
        right_triangle_title = MathTex(r"\text{主要关注直角三角形}", color=BLUE_D).scale(1.2).to_edge(UP, buff=0.7)
        self.play(Write(right_triangle_title), run_time=0.8)
        self.wait(0.3)

        # Draw a right triangle and define an angle theta
        p1 = LEFT * 4 + DOWN * 2
        p2 = RIGHT * 0 + DOWN * 2
        p3 = LEFT * 4 + UP * 2
        right_triangle = Polygon(p1, p2, p3, color=PURPLE, fill_opacity=0.3, stroke_width=5)
        right_angle_square = Square(side_length=0.4, color=YELLOW, fill_opacity=1).move_to(p1, DR).shift(RIGHT * 0.2 + UP * 0.2)
        theta_label = MathTex(r"\theta", color=RED).move_to(p3 + RIGHT * 0.5 + DOWN * 0.5)

        self.play(Create(right_triangle), Create(right_angle_square), FadeIn(theta_label), run_time=1.5)
        self.wait(0.3)

        # Label sides concurrently
        hypotenuse_line = Line(p2, p3, color=GREEN_B, stroke_width=7)
        opposite_line = Line(p1, p2, color=ORANGE, stroke_width=7)
        adjacent_line = Line(p1, p3, color=TEAL, stroke_width=7)

        hypotenuse_text = MathTex(r"\text{斜边}", color=GREEN_B).next_to(hypotenuse_line, RIGHT, buff=0.2).shift(UP*0.2)
        opposite_text = MathTex(r"\text{对边}", color=ORANGE).next_to(opposite_line, DOWN, buff=0.2)
        adjacent_text = MathTex(r"\text{邻边}", color=TEAL).next_to(adjacent_line, LEFT, buff=0.2)

        self.play(
            Create(hypotenuse_line), Write(hypotenuse_text),
            Create(opposite_line), Write(opposite_text),
            Create(adjacent_line), Write(adjacent_text),
            run_time=2
        )
        self.wait(0.5)

        self.play(
            FadeOut(right_triangle_title, right_triangle, right_angle_square, theta_label,
                    hypotenuse_line, opposite_line, adjacent_line,
                    hypotenuse_text, opposite_text, adjacent_text),
            run_time=0.8
        )
        self.clear()

        # --- Scene 3: Basic Trigonometric Ratios ---
        ratios_title = MathTex(r"\text{基本三角比}", color=BLUE_D).scale(1.2).to_edge(UP, buff=0.7)
        self.play(Write(ratios_title), run_time=0.8)
        self.wait(0.3)

        # Redraw a simpler right triangle for ratios
        p1_r = LEFT * 3 + DOWN * 1.5
        p2_r = RIGHT * 1 + DOWN * 1.5
        p3_r = LEFT * 3 + UP * 1.5
        ratio_triangle = Polygon(p1_r, p2_r, p3_r, color=PURPLE, fill_opacity=0.3, stroke_width=5)
        ratio_right_angle = Square(side_length=0.4, color=YELLOW, fill_opacity=1).move_to(p1_r, DR).shift(RIGHT * 0.2 + UP * 0.2)
        ratio_theta_label = MathTex(r"\theta", color=RED).move_to(p3_r + RIGHT * 0.5 + DOWN * 0.5)

        hyp_label_short = MathTex(r"\text{斜边}", color=GREEN_B).next_to(Line(p2_r, p3_r), RIGHT, buff=0.2).shift(UP*0.2)
        opp_label_short = MathTex(r"\text{对边}", color=ORANGE).next_to(Line(p1_r, p2_r), DOWN, buff=0.2)
        adj_label_short = MathTex(r"\text{邻边}", color=TEAL).next_to(Line(p1_r, p3_r), LEFT, buff=0.2)

        self.play(
            Create(ratio_triangle), Create(ratio_right_angle), FadeIn(ratio_theta_label),
            FadeIn(hyp_label_short, opp_label_short, adj_label_short),
            run_time=1.5
        )
        self.wait(0.3)

        # Display ratios
        sin_formula = MathTex(
            r"\sin(\theta) = \frac{\text{对边}}{\text{斜边}}",
            color=BLACK
        ).scale(0.7).next_to(ratios_title, DOWN, buff=0.8).align_to(LEFT, edge=LEFT).shift(RIGHT*1.5)

        cos_formula = MathTex(
            r"\cos(\theta) = \frac{\text{邻边}}{\text{斜边}}",
            color=BLACK
        ).scale(0.7).next_to(sin_formula, DOWN, buff=0.4).align_to(sin_formula, LEFT)

        tan_formula = MathTex(
            r"\tan(\theta) = \frac{\text{对边}}{\text{邻边}}",
            color=BLACK
        ).scale(0.7).next_to(cos_formula, DOWN, buff=0.4).align_to(sin_formula, LEFT)

        self.play(Write(sin_formula), run_time=0.8)
        self.play(Write(cos_formula), run_time=0.8)
        self.play(Write(tan_formula), run_time=0.8)
        self.wait(0.8)

        self.play(
            FadeOut(ratios_title, ratio_triangle, ratio_right_angle, ratio_theta_label,
                    hyp_label_short, opp_label_short, adj_label_short,
                    sin_formula, cos_formula, tan_formula),
            run_time=0.8
        )
        self.clear()

        # --- Scene 4: Example 1 - Simple Calculation ---
        example1_title = MathTex(r"\text{例1: 简单计算}", color=BLUE_D).scale(1.2).to_edge(UP, buff=0.7)
        self.play(Write(example1_title), run_time=0.8)
        self.wait(0.3)

        # Draw a right triangle with specific sides
        p1_ex1 = LEFT * 3 + DOWN * 1.5
        p2_ex1 = RIGHT * 1 + DOWN * 1.5
        p3_ex1 = LEFT * 3 + UP * 1.5
        ex1_triangle = Polygon(p1_ex1, p2_ex1, p3_ex1, color=PURPLE, fill_opacity=0.3, stroke_width=5)
        ex1_right_angle = Square(side_length=0.4, color=YELLOW, fill_opacity=1).move_to(p1_ex1, DR).shift(RIGHT * 0.2 + UP * 0.2)

        # Side lengths and angle theta
        side_a_val = MathTex(r"3", color=ORANGE).next_to(Line(p1_ex1, p2_ex1), DOWN, buff=0.2)
        side_b_val = MathTex(r"4", color=TEAL).next_to(Line(p1_ex1, p3_ex1), LEFT, buff=0.2)
        side_c_val = MathTex(r"5", color=GREEN_B).next_to(Line(p2_ex1, p3_ex1), RIGHT, buff=0.2).shift(UP*0.2)
        ex1_theta_label = MathTex(r"\theta", color=RED).move_to(p3_ex1 + RIGHT * 0.5 + DOWN * 0.5)

        self.play(
            Create(ex1_triangle), Create(ex1_right_angle),
            FadeIn(side_a_val, side_b_val, side_c_val, ex1_theta_label),
            run_time=1.5
        )
        self.wait(0.3)

        # Calculations
        calc_sin = MathTex(r"\sin(\theta) = \frac{3}{5} = 0.6", color=BLACK).scale(0.6).next_to(ex1_triangle, RIGHT, buff=0.8).align_to(ex1_triangle, UP).shift(UP*0.5)
        calc_cos = MathTex(r"\cos(\theta) = \frac{4}{5} = 0.8", color=BLACK).scale(0.6).next_to(calc_sin, DOWN, buff=0.3).align_to(calc_sin, LEFT)
        calc_tan = MathTex(r"\tan(\theta) = \frac{3}{4} = 0.75", color=BLACK).scale(0.6).next_to(calc_cos, DOWN, buff=0.3).align_to(calc_sin, LEFT)

        self.play(Write(calc_sin), run_time=0.6)
        self.play(Write(calc_cos), run_time=0.6)
        self.play(Write(calc_tan), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(example1_title, ex1_triangle, ex1_right_angle,
                    side_a_val, side_b_val, side_c_val, ex1_theta_label,
                    calc_sin, calc_cos, calc_tan),
            run_time=0.8
        )
        self.clear()

        # --- Scene 5: Example 2 - Real-world Application (Height of a building) ---
        example2_title = MathTex(r"\text{例2: 测量建筑物高度}", color=BLUE_D).scale(1.2).to_edge(UP, buff=0.7)
        self.play(Write(example2_title), run_time=0.8)
        self.wait(0.3)

        # Draw ground, building, and observer
        ground = Line(LEFT * 6, RIGHT * 6, color=BROWN, stroke_width=5).to_edge(DOWN, buff=1.5)
        building = Line(ground.get_left() + RIGHT * 2, ground.get_left() + RIGHT * 2 + UP * 4, color=GRAY_D, stroke_width=8)
        observer = Dot(ground.get_right() + LEFT * 2, color=RED).scale(1.5)
        observer_label = MathTex(r"\text{观察者}", color=RED).next_to(observer, DOWN, buff=0.2).scale(0.7)

        self.play(Create(ground), Create(building), Create(observer), Write(observer_label), run_time=1.2)
        self.wait(0.3)

        # Angle of elevation, known distance, unknown height
        line_of_sight = Line(observer.get_center(), building.get_top(), color=BLUE_C, stroke_width=3)
        angle_arc = Arc(radius=0.8, start_angle=line_of_sight.get_angle(), angle=building.get_bottom().get_angle() - line_of_sight.get_angle(), arc_center=observer.get_center(), color=RED)
        angle_theta_label = MathTex(r"30^\circ", color=RED).move_to(angle_arc.get_center() + UP * 0.3 + LEFT * 0.3).scale(0.7)

        distance_line = Line(observer.get_center(), building.get_bottom(), color=TEAL, stroke_width=3)
        distance_label = MathTex(r"100\text{米}", color=TEAL).next_to(distance_line, DOWN, buff=0.2).scale(0.7)

        height_label = MathTex(r"h", color=ORANGE).next_to(building, LEFT, buff=0.2).scale(0.7)

        self.play(
            Create(line_of_sight), Create(angle_arc), Write(angle_theta_label),
            Create(distance_line), Write(distance_label), Write(height_label),
            run_time=1.8
        )
        self.wait(0.3)

        # Explain using tangent
        tan_explanation = VGroup(
            MathTex(r"\tan(\theta) = \frac{\text{对边}}{\text{邻边}}", color=BLACK),
            MathTex(r"\tan(30^\circ) = \frac{h}{100}", color=BLACK),
            MathTex(r"h = 100 \times \tan(30^\circ)", color=BLACK),
            MathTex(r"h \approx 100 \times 0.577", color=BLACK),
            MathTex(r"h \approx 57.7\text{米}", color=BLACK)
        ).scale(0.6).arrange(DOWN, buff=0.2).next_to(building, RIGHT, buff=0.8).align_to(building, UP).shift(UP*0.5)

        self.play(Write(tan_explanation[0]), run_time=0.6)
        self.play(Write(tan_explanation[1]), run_time=0.6)
        self.play(Write(tan_explanation[2]), run_time=0.6)
        self.play(Write(tan_explanation[3]), run_time=0.6)
        self.play(Write(tan_explanation[4]), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(example2_title, ground, building, observer, observer_label,
                    line_of_sight, angle_arc, angle_theta_label,
                    distance_line, distance_label, height_label,
                    tan_explanation),
            run_time=0.8
        )
        self.clear()

        # --- Final Scene: Summary ---
        final_message = MathTex(
            r"\text{三角学：理解角度与边的强大工具！}",
            color=BLUE_D
        ).scale(1.2)
        self.play(Write(final_message), run_time=1.2)
        self.wait(0.8)
        self.play(FadeOut(final_message), run_time=0.5)
        self.wait(0.3)