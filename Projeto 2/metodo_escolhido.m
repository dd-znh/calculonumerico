function retval = metodo_escolhido(y1, y2, g, L, h, T)
    theta = y1;
    omega = y2;
    for i = 1:1000
        k1_theta = omega;
        k1_omega = func(theta);

        k2_theta = omega + (h/2) * k1_omega;
        k2_omega = func(theta + (h/2) * k1_theta);

        k3_theta = omega + (h/2) * k2_omega;
        k3_omega = func(theta + (h/2) * k2_theta);

        k4_theta = omega + h * k3_omega;
        k4_omega = func(theta + h * k3_theta);

        theta = theta + (h/6) * (k1_theta + 2*k2_theta + 2*k3_theta + k4_theta);
        omega = omega + (h/6) * (k1_omega + 2*k2_omega + 2*k3_omega + k4_omega);
    end
    retval = theta;
endfunction

function retval = func(x)
    g = 9.81;
    L = 0.1;
    retval = - (g / L) * sin(x);
endfunction