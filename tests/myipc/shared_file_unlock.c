/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * file_shared_unlock.c
 * Copyright (C) 2025 Vladimir Roncevic <elektron.ronca@gmail.com>
 *
 * myipc is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * myipc is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */
#include "shared_file.h"

int file_shared_unlock(int fd, struct flock *lock)
{
    //////////////////////////////////////////////////////////////////////////
    /// Checks if the shared file descriptor is valid
    if (fd < 0)
    {
        perror("Invalid shared file descriptor.");
        return SHARED_FILE_ERROR;
    }

    //////////////////////////////////////////////////////////////////////////
    /// Checks if the buffer pointer is valid
    if (lock == NULL)
    {
        perror("Invalid lock pointer provided.");
        return SHARED_FILE_ERROR;
    }

    //////////////////////////////////////////////////////////////////////////
    /// Releases the lock
    lock->l_type = F_UNLCK;

    int status = fcntl(fd, F_SETLK, lock);

    if (status < 0)
    {
        perror("Failed to unlock shared file.");
        return SHARED_FILE_ERROR;
    }

    return SHARED_FILE_SUCCESS;
}
