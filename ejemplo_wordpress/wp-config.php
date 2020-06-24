<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

define('WP_HOME','https://idtel-store.tech');

define('WP_SITEURL','https://idtel-store.tech');

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** MySQL database username */
define( 'DB_USER', 'wordpress' );

/** MySQL database password */
define( 'DB_PASSWORD', '96c4de313b00f565cd02f664abd201631dec72c344c65c5d' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'mdeXmBS6+MLC<e2o.xTvwxAcy:7a[D/#V]Ri.?LWjNl/lU|V}qD75i(47_MZfm#A' );
define( 'SECURE_AUTH_KEY',  'LZHz/gx+o|aiwrStdez(Vt{VPaPS}_eRB9/N)5ch#gIzqZ@*|;:1,~zU[7TgUpX~' );
define( 'LOGGED_IN_KEY',    '~=v VfF^dQ9l>.iEcAO34OM2ER*/uwH%~r#1mb8Om[-v7EoWe6AH]P.0*xjDif-%' );
define( 'NONCE_KEY',        'UIL[Q(D)pB/m@yCk>GgSqd*^,;%li`fI_CyTC^qb7:jW*]7d%R/VNJy@#oVS=E_5' );
define( 'AUTH_SALT',        'h:R `]g 9R9T<0mKmOx548,^=-wH/A_]r5Lbw>M;MY:#>1{&W}L&5Xi) `:p-X,[' );
define( 'SECURE_AUTH_SALT', 'pZOUW<-/K:PNyU|_kTpwpb[;4>!-q>vW7_9tSHAo?DyGKWt=F08vE#@q*=u D>Y9' );
define( 'LOGGED_IN_SALT',   '5j+*vXcSv&ZnX^3c uu?6-`L_9w{YL)w-P(ZU_0{KmR+(xq=ni|E%y7$*py#k{,~' );
define( 'NONCE_SALT',       'SL9![hnsmmhfduDAm-6mz}d?+lRY<vh6)|`J #2tOW!r-#->Al[ecQT2>j!R]d~t' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );
}

/** Sets up WordPress vars and included files. */
require_once( ABSPATH . 'wp-settings.php' );

define( 'WP_ALLOW_REPAIR', true);
