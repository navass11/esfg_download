from math import *
def rotated_grid_transform(grid_in, option, SP_coor):
    lon = grid_in[0]
    lat = grid_in[1];

    lon = (lon*pi)/180; # Convert degrees to radians
    lat = (lat*pi)/180;

    SP_lon = SP_coor[0];
    SP_lat = SP_coor[1];
    
    #SP_lon = NP_lon - 180, SP_lat = -NP_lat.

    theta = 90+SP_lat; # Rotation around y-axis
    phi = SP_lon; # Rotation around z-axis

    theta = (theta*pi)/180;
    phi = (phi*pi)/180; # Convert degrees to radians

    x = np.cos(lon)*np.cos(lat); # Convert from spherical to cartesian coordinates
    y = np.sin(lon)*np.cos(lat);
    z = np.sin(lat);

    if option == 1: # Regular -> Rotated

        x_new = np.cos(theta)*np.cos(phi)*x + np.cos(theta)*np.sin(phi)*y + np.sin(theta)*z;
        y_new = -np.sin(phi)*x + np.cos(phi)*y;
        z_new = -np.sin(theta)*np.cos(phi)*x - np.sin(theta)*np.sin(phi)*y + np.cos(theta)*z;

    else:  # Rotated -> Regular

        phi = -phi;
        theta = -theta;

        x_new = np.cos(theta)*np.cos(phi)*x + np.sin(phi)*y + np.sin(theta)*np.cos(phi)*z;
        y_new = -np.cos(theta)*np.sin(phi)*x + np.cos(phi)*y - np.sin(theta)*np.sin(phi)*z;
        z_new = -np.sin(theta)*x + np.cos(theta)*z;



    lon_new = np.arctan2(y_new,x_new); # Convert cartesian back to spherical coordinates
    lat_new = np.arcsin(z_new);

    lon_new = (lon_new*180)/pi; # Convert radians back to degrees
    lat_new = (lat_new*180)/pi;

    return lon_new , lat_new
